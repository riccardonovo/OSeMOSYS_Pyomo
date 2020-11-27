from __future__ import division
import sys
from input_dat_generation import dat_generation
from osemosys_func import osemosys_model
from pyomo.opt import SolverStatus, TerminationCondition

## FILES PATHS
file_sets = "1_SETS.xlsx"
file_parameters = r"2_PARAMETERS.xlsx"
file_dat = r"Input.dat"
file_json = r"results.json"

## SOLVER
solver = 'cplex'

# ## GENERATION OF THE .dat INPUT FILE
dat_generation(file_sets, file_parameters, file_dat)
print("Input .dat file has been generated")

# ## BUILDING AND SOLVING THE OSeMOSYS MODEL
model, instance, results = osemosys_model(file_dat, file_json, solver)
print("Model has been built and solved")

if (results.solver.status != SolverStatus.ok) or (results.solver.termination_condition != TerminationCondition.optimal):
    # Do something when the solution in non optimal or infeasible
    print("Solver status : ", results.solver.status)
    print("Termination condition : ", results.solver.termination_condition)
    print("Quitting the execution")
    sys.exit()
