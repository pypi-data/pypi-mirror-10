#! /usr/bin/python
from __future__ import absolute_import as _absolute_import

'''
Copyright 2015 Tim Nonner

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

import time, copy, collections
import pulp as pl

def _isnumeric(var) :
	return isinstance(var,(int)) # only integers are accepted

def _solve_mip(mip,kind='CBC',time_limit=None,msg=0) :

	start_time = time.time()
	# select solver for pl
	if kind == 'CPLEX' :
		if time_limit :
			# pulp does currently not support a timelimit in 1.5.9
			mip.solve(pl.CPLEX_CMD(msg=msg,timelimit=time_limit))
		else :
			mip.solve(pl.CPLEX_CMD(msg=msg))
	elif kind == 'GLPK' :
		mip.solve(pl.GLPK_CMD(msg=msg))
	elif kind == 'CBC' :
		options = []
		if time_limit :
			options += ['sec',str(time_limit)]
		mip.solve(pl.PULP_CBC_CMD(msg=msg,options=options))
	else :
		raise Exception('ERROR: solver '+kind+' not known')

	if msg :
		print('INFO: execution time for solving mip (sec) = '+str(time.time()-start_time))
	if mip.status == 1 and msg :		
		print('INFO: objective = '+str(pl.value(mip.objective)))


def solve(scenario,big_m=10000,kind='CBC',time_limit=None,msg=0,return_copy=False) :
	"""
	Shortcut to continuous mip
	"""
	if return_copy :
		scenario = copy.deepcopy(scenario)
	ContinuousMIP().solve(scenario,big_m=big_m,kind=kind,time_limit=time_limit,msg=msg)
	return scenario


def solve_discrete(scenario,horizon,kind='CBC',time_limit=None,task_groups=None,msg=0,return_copy=False) :
	"""
	Shortcut to discrete mip
	"""
	if return_copy :
		scenario = copy.deepcopy(scenario)
	DiscreteMIP().solve(scenario,horizon,kind=kind,time_limit=time_limit,task_groups=task_groups,msg=msg)
	return scenario


class ContinuousMIP(object) :
	"""
	An interface to the pulp MIP solver package, supported are CPLEX, GLPK, CBC
	"""

	def __init__(self) :
		self.scenario = None
		self.big_m = None
		self.mip = None
		self.x = None  # mip variables shortcut


	def build_mip_from_scenario(self,task_groups=None,msg=0) :

		S = self.scenario
		BIG_M = self.big_m #TODO: GLPK has problems with large number
		mip = pl.LpProblem(str(S), pl.LpMinimize)

		# check for objective
		if not S.objective() :
			if msg : print('INFO: use makespan objective as default')
			S.use_makespan_objective()

		# task variables
		x = dict()

		for T in S.tasks() :
			x[T] = pl.LpVariable(T,0)

			# fix variables if start is given (0.0 is also False!)
			if T.start is not None :
				mip += x[T] == T.start

			# add assignment variable for each possible resource
			# if resources are fixed take only these
			if T.resources :
				for R in T.resources :
					x[(T,R)] = pl.LpVariable((T,R),0,1,cat=pl.LpBinary)
					mip += x[(T,R)] == 1
			else :
				for R in T.resources_req.resources() :
					x[(T,R)] = pl.LpVariable((T,R),0,1,cat=pl.LpBinary)
				# everybody is required on one resource from each or clause
				for RA in T.resources_req :
					mip += sum([ x[(T,R)] for R in RA ]) == 1

		# objective
		objective = S.objective()
		mip += sum([ x[T]*objective[T] for T in objective if T in x ])

		# resource capacity constraints
		for R in S.resources() :
			if R.capacity :
				mip += sum([ x[(T,R)]*T.resources_req.capacity_req(R) for T in S.tasks() \
		                               if R in T.resources_req.resources() ]) <= R.capacity

		# same resource variable
		task_pairs = [ (T,T_) for T in S.tasks() for T_ in S.tasks() if str(T) < str(T_) ]
		for (T,T_) in task_pairs :
			if T.resources :
				resources = T.resources
			else :
				resources = T.resources_req.resources()
			if T_.resources :
				resources_ = T_.resources
			else :
				resources_ = T_.resources_req.resources()
			shared_resources = list( set(resources) & set(resources_) )
			# TODO: restrict the number of variables
			if shared_resources and (T.start is None or T_.start is None ) :
				x[(T,T_,'SameResource')] = pl.LpVariable((T,T_,'SameResource'),lowBound=0)#,cat=pl.LpInteger)
				x[(T_,T,'SameResource')] = pl.LpVariable((T_,T,'SameResource'),lowBound=0)#,cat=pl.LpInteger)
				mip += x[(T,T_,'SameResource')] == x[(T_,T,'SameResource')]
				for R in shared_resources :
					mip += x[(T,R)] + x[(T_,R)] - 1 <= x[(T,T_,'SameResource')]
				# ordering variables
				x[(T,T_)] = pl.LpVariable((T,T_),0,1,cat=pl.LpBinary)
				x[(T_,T)] = pl.LpVariable((T_,T),0,1,cat=pl.LpBinary)
				mip += x[(T,T_)] + x[(T_,T)] == 1

				mip += x[T] + T.length <= x[T_] + (1-x[(T,T_)])*BIG_M + (1-x[(T,T_,'SameResource')])*BIG_M 
				mip += x[T_] + T_.length <= x[T] + x[(T,T_)]*BIG_M + (1-x[(T,T_,'SameResource')])*BIG_M
			
		
		# precedence constraints
		for P in S.precs_lax() :
			# if at least one of the tasks is not fixed
			if P.left.start is None or P.right.start is None :
				mip += x[P.left] + P.left.length + P.offset <= x[P.right] 
	
	
		# tight precedence constraints
		for P in S.precs_tight() :
			# if at least one of the tasks is not fixed
			if P.left.start is None and P.right.start is None :
				mip += x[P.left] + P.left.length + P.offset == x[P.right] 

		# TODO: not set if not on same resource??
		# conditional precedence constraints
		for P in S.precs_cond() :
			# if at least one of the tasks is not fixed
			if P.left.start is None and P.right.start is None :
				mip += x[P.left] + P.left.length + P.offset <= x[P.right] + \
			                (1-x[(P.left,P.right)])*BIG_M + (1-x[(P.left,P.right,'SameResource')])*BIG_M

		# upper bounds
		for P in S.precs_up() :
			# if start is not fixed
			if P.left.start is None :
				mip += x[P.left] + P.left.length <= P.right

		# lower bounds
		for P in S.precs_low() :
			# if start is not fixed
			if P.left.start is None :
				mip += x[P.left] >= P.right

		self.mip = mip
		self.x = x


	def read_solution_from_mip(self,msg=0) :
		for T in self.scenario.tasks() :
			T.start = self.x[T].varValue
			if T.resources :
				resources = T.resources
			else :
				resources = T.resources_req.resources()
			T.resources = [ R for R in resources if self.x[(T,R)].varValue > 0 ]


	def solve(self,scenario,big_m=10000,kind='CBC',time_limit=None,msg=0) :
		"""
		Solves the given scenario using a continous MIP via the pulp package

		Args:
			scenario:    scenario to solve
			kind:        MIP-solver to use: CPLEX, GLPK, CBC
			big_m :      a large number to allow a big-m type model
			time_limit:  a time limit, only for CPLEX and CBC
			msg:         0 means no feedback (default) during computation, 1 means feedback
	
		Returns:
			scenario is solving was successful
			None if solving was not successful
		"""
		self.scenario = scenario
		self.big_m = big_m
		self.build_mip_from_scenario(msg=msg)
		_solve_mip(self.mip, kind=kind, time_limit=time_limit, msg=msg)

		if self.mip.status != 1 :
			if msg : print('ERROR: no solution found')
			#return None #TODO: problem sometimes still returned 0 when solution found

		self.read_solution_from_mip(msg=msg)
		return self.scenario


class DiscreteMIP(object) :
	"""
	pulp with time discretisation
	"""

	def __init__(self) :
		self.scenario = None
		self.horizon = None
		self.task_groups = None
		self.mip = None
		self.x = None  # mip variables shortcut


	def build_mip_from_scenario(self,msg=0) :
		S = self.scenario
		mip = pl.LpProblem(str(S), pl.LpMinimize)

		# check for objective
		if not S.objective() :
			if msg : print('INFO: use makespan objective as default')
			S.use_makespan_objective()
		
		# organize task groups
		if self.task_groups == None :
			self.task_groups = collections.OrderedDict()
		tasks_in_groups = set([ T_ for T in self.task_groups for T_ in self.task_groups[T] ])
		for T in S.tasks() :
			if T not in tasks_in_groups :
				self.task_groups[T] = [T]
		task_to_group = { T_ : T for T in self.task_groups for T_ in self.task_groups[T] }

		x = dict() # mip variables
		cons = list() # mip constraints
		self.task_groups_free = list()
		for T in self.task_groups :
			task_group_size = len(self.task_groups[T])
			if T.start is None or task_group_size > 1 :
				self.task_groups_free.append(T)

				'''
				# base time-indexed variables for task group
				for t in range(self.horizon) :
					x[T,t] = pl.LpVariable((T,t),0,task_group_size) # continous variables
				# lower and upper boundary conditions
				cons.append( pl.LpConstraint( x[T,0], sense=0, rhs=task_group_size ) )
				cons.append( pl.LpConstraint( x[T,self.horizon-1], sense=0, rhs=0 ) ) #required for no solution feedback
				'''

				# generate variabels for task resources
				for R in T.resources_req.resources() :
					# resource base variables
					for t in range(self.horizon) :
						x[T,R,t] = pl.LpVariable((T,R,t),0,task_group_size,cat=pl.LpInteger) #binary or not?
					# monotonicity (base variables should inherit this)
					for t in range(self.horizon-1) :
						cons.append( pl.LpConstraint( pl.LpAffineExpression([ (x[T,R,t],1), (x[T,R,t+1],-1) ]), sense=1, rhs=0 ) )

				for t in range(self.horizon) :
					RA = T.resources_req[0]
					x[T,t] = pl.LpAffineExpression([ (x[T,R,t],1) for R in RA ])
				cons.append( x[T,0] == task_group_size )
				cons.append( x[T,self.horizon-1] == 0 ) #required for no solution feedback

			
				# consider each resource selection
				for RA in T.resources_req[1:] :
					# resource base variables should match base variables in each time step
					for t in range(self.horizon) :
						affine = pl.LpAffineExpression([ (x[T,R,t],1) for R in RA ])
						cons.append( affine == x[T,t] )

				'''
				# fix variables if start is given
				starts = [ T_.start for T_ in self.task_groups[T] if T_.start is not None ]
				if starts and max(starts) > self.horizon :
						raise Exception('ERROR: fixed start of task '+str(T)+' larger than max time step '+str(horizon))
				for t in starts : 
					starts_after_t = [ t_ for t_ in starts if t_ >= t ]
					cons.append( x[T,t] - x[T,t+1] >= len(starts_after_t) )
					#cons.append( pl.LpConstraint( pl.LpAffineExpression([ (x[T,t],1), (x[T,t+1],-1) ]), sense=1, rhs=len(starts_after_t) ) )
				'''

				# fix resources if they are given
				# TODO: fixed resources not really tested
				'''
				resources = [ R for T_ in self.task_groups[T] if T_.resources for R in T_.resources ]
				for R in resources :
					if R in T.resources_req.resources() :
						cons.append( pl.LpConstraint( pl.LpAffineExpression([ (x[T,R,0],1) ]), sense=1, rhs=resources.count(R) ) )
					else :
						raise Exception('ERROR: resource '+str(R)+' is not part of the requirements for task '+str(T))
				'''
				
		# respect fixed tasks, they can block free tasks
		# TODO: all precs need to get translated into relations between fixed and free tasks
		# TODO: currently fixed tasks are only blockers, not suitable for list scheduling
		for T in set(self.task_groups) - set(self.task_groups_free)  :
			t_start = T.start
			t_end = min(T.start+T.length,self.horizon-1)
			for R in T.resources :
				resource_tasks = [ T_ for T_ in self.task_groups_free if R in T_.resources_req.resources() ]
				affine = pl.LpAffineExpression([ (x[T_,R,max(t_start-T_.length,0)],1) for T_ in resource_tasks ]+\
                                                               [ (x[T_,R,t_end],-1) for T_ in resource_tasks ])
				cons.append( pl.LpConstraint( affine, sense=0, rhs=0 ) )

		# objective
		objective = S.objective()
		objective_tasks = [ T for T in set(objective) & set(self.task_groups_free) ]
		objective_resources = [ R for R in set(objective) & set(self.scenario.resources()) ]
		for R in objective_resources :
			resource_upper_bound = len(self.scenario.tasks())
			x[R] = pl.LpVariable('resource_'+str(R)+'_switch',0,1,cat=pl.LpBinary)
			affine = pl.LpAffineExpression( [ ( x[T,R,0], 1) for T in self.task_groups_free if R in T.resources_req.resources() ] + 
                                                        [ ( x[R],-resource_upper_bound) ] )
			cons.append( pl.LpConstraint( affine, sense=-1, rhs=0.0 ) )
		mip += sum([ x[T,t]*objective[T] for T in objective_tasks for t in range(self.horizon) ]) + \
	                 pl.LpAffineExpression([ ( x[R], objective[R]) for R in objective_resources ])

		#pl.LpAffineExpression([ ( x[T,t], objective[T]) for T in objective_tasks for t in range(self.horizon)  ] +
                                            

		# resource non-overlapping constraints 
		for R in S.resources() :
			resource_tasks = [ T for T in self.task_groups_free if R in T.resources_req.resources() ]
			for t in range(self.horizon) :
				affine = pl.LpAffineExpression([ (x[T,R,max(t-T.length,0)], 1) for T in resource_tasks ] + \
                                                               [ (x[T,R,t], -1) for T in resource_tasks ])
				cons.append( pl.LpConstraint( affine, sense=-1, rhs=1.0 ) )
			# resource capacity
			if R.capacity :
				resource_tasks = [ T for T in self.task_groups_free \
                                                   if R in T.resources_req.resources() ]
				# get lower and upper capacity bound
				if _isnumeric(R.capacity) :
					min_capacity = 0
					max_capacity = R.capacity
				else :
					min_capacity = R.capacity[0]
					max_capacity = R.capacity[1]
				# implement lower capacity bound
				if min_capacity > 0 :
					affine = pl.LpAffineExpression([ (x[T,R,0],T.resources_req.capacity_req(R)) for T in resource_tasks ])
					cons.append( pl.LpConstraint( affine, sense=1, rhs=min_capacity ) )
				# implement upper capacity
				affine = pl.LpAffineExpression([ (x[T,R,0],T.resources_req.capacity_req(R)) for T in resource_tasks ])
				cons.append( pl.LpConstraint( affine, sense=-1, rhs=max_capacity ) )

		# precedence constraints
		for P in S.precs_lax() :
			if P.left in self.task_groups and P.right in self.task_groups :
				left_size = float(len(self.task_groups[P.left]))
				right_size = float(len(self.task_groups[P.right]))
				if P.left in self.task_groups_free and P.right in self.task_groups_free : #TODO: take care of all other cases -> treat as prec_low and prec_up
					for t in range(self.horizon) :

						cons.append( x[P.left,t]/left_size <= x[P.right,min(t+P.left.length+P.offset,self.horizon-1) ] )
						#affine = pl.LpAffineExpression([ ( x[P.left,t], 1/left_size), (x[P.right,min(t+P.left.length+P.offset,self.horizon-1)],-1/right_size)  ])
						#cons.append( pl.LpConstraint( affine, sense=-1, rhs=0 ) )
	
		# tight precedence constraints
		for P in S.precs_tight() :
			if P.left in self.task_groups and P.right in self.task_groups :
				left_size = float(len(self.task_groups[P.left]))
				right_size = float(len(self.task_groups[P.right]))
				for t in range(self.horizon) :
					cons.append( x[P.left,t]/left_size == x[P.right,min(t+P.left.length+P.offset,self.horizon-1) ] )
					#affine = pl.LpAffineExpression([ ( x[P.left,t], 1/left_size), (x[P.right,min(t+P.left.length,self.horizon-1)],-1/right_size)  ])
					#cons.append( pl.LpConstraint( affine, sense=0, rhs= -P.offset ) )

		'''
		# conditional precedence constraints
		for P in S.precs_cond() :
			if P.left in self.task_groups and P.right in self.task_groups :
				left_size = float(len(self.task_groups[P.left]))
				right_size = float(len(self.task_groups[P.right]))
				shared_resources = list( set(P.left.resources_req.resources()) & set(P.right.resources_req.resources()) )
				for R in shared_resources :	
					for t in range(self.horizon) :
						affine = pl.LpAffineExpression([ ( x[P.left,R,max(t-P.left.length,0)],1 ), (x[P.left,R,t],-1),\
				                                                 ( x[P.right,R,max(t-P.left.length,0)], 1), (x[P.right,R,min(t+P.offset,self.horizon-1)],-1) ])
						cons.append( pl.LpConstraint( affine, sense=-1, rhs=1 ) )
		'''
	
		'''
		# lower bounds
		for P in S.precs_low() :
			if P.left in self.task_groups :
				cons.append( x[P.left,P.right] == len(self.task_groups[T]) )

		# upper bounds
		for P in S.precs_up() :
			if P.left in self.task_groups :
				cons.append( x[P.left,P.right] == 0 )
		'''

		# ensure that tasks with similar precedences are run on the same resources
		same_resource_precs = list()
		if self.scenario.is_same_resource_precs_lax :
			same_resource_precs.extend(S.precs_lax())
		if self.scenario.is_same_resource_precs_tight :
			same_resource_precs.extend(S.precs_tight())
		for P in same_resource_precs :
			if P.left in self.task_groups and P.right in self.task_groups :
				shared_resources = set(P.left.resources_req.resources()) & set(P.right.resources_req.resources())
				for R in shared_resources :
					for t in range(self.horizon) :
						affine = pl.LpAffineExpression([ ( x[(P.left,R,t)],1 ), (x[(P.right,R,t)],-1) ])
						con = pl.LpConstraint( affine, sense=-1, rhs=0 )
						cons.append(con)

		for con in cons :
			mip.addConstraint(con)

		self.mip = mip
		self.x = x


	def read_solution_from_mip(self,msg=0) :
				
		for T in self.task_groups_free :

			print('#############',T)

			starts = [ max([ t for t in range(self.horizon) if sum([ v.varValue for v in self.x[T,t] ]) >= z-0.5 ]) \
                                   for z in range(int( sum([ v.varValue for v in self.x[T,0] ]) ),0,-1) ]
			RA_resources = collections.OrderedDict()
			RA_starts = collections.OrderedDict()
			for RA in T.resources_req :
				RA_starts[RA] = list()
				for R in RA :
					R_starts = [ max([ t for t in range(self.horizon) if self.x[(T,R,t)].varValue >= z-0.5 ]) \
		                                     for z in range(int(self.x[(T,R,0)].varValue),0,-1) ]
					RA_starts[RA].extend( [ (t,R) for t in R_starts ] )
				RA_starts[RA] = sorted(RA_starts[RA])
				RA_resources[RA] = [ (t,R) for t,R in RA_starts[RA] ]

			# check for predefined starts
			for T_ in self.task_groups[T] :
				if T_.start is not None :
					starts.remove(T_.start)
				if T_.resources is not None :
					for R in T_.resources :
						for RA in T.resources_req :
							RA_resources[RA].remove(R)

			#print( { R : [ self.x[T,R,t].varValue for t in range(20) ] for R in T.resources_req.resources() } )
			#import pdb;pdb.set_trace()
			#if T.name == 'KMT_0' :

			#print({ R : [ self.x[T,R,t].varValue for t in range(10) ] for R in T.resources_req.resources() })
			#import pdb;pdb.set_trace()
				

			start_count = 0
			resource_count = 0		
			for T_ in self.task_groups[T] :
				if T_.start is None :
					T_.start = starts[start_count]
					start_count += 1
				if T_.resources is None :
					T_.resources = []
					for RA in T.resources_req :
						T_.resources.append(RA_resources[RA][resource_count][1])
					resource_count += 1


	def solve(self,scenario,horizon='100',kind='CBC',time_limit=None,task_groups=None,msg=0) :
		"""
		Solves the given scenario using a discrete MIP via the pulp package

		Args:
			scenario:            scenario to solve
			kind:                MIP-solver to use: CPLEX, GLPK, CBC
			horizon :            the number of time steps to model
			time_limit:          a time limit, only for CPLEX and CBC
                        task_groups:         a dictionary that clusters the tasks into identical ones,
                                             the key of each cluster must be a representative
			msg:                 0 means no feedback (default) during computation, 1 means feedback
	
		Returns:
			scenario is solving was successful
			None if solving was not successful
		"""

		self.scenario = scenario
		self.horizon = horizon
		self.task_groups = task_groups
		self.build_mip_from_scenario(msg=msg)
		_solve_mip(self.mip,kind=kind,time_limit=time_limit,msg=msg)

		if self.mip.status != 1 :
			if msg : print ('ERROR: no solution found')
			#return None #TODO: problem sometimes still returned 0 when solution found

		self.read_solution_from_mip(msg=msg)	
		return self.scenario ##TODO: check what to return
	









