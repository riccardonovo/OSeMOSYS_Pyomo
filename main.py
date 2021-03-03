""" 
Script developed @ the Energy Center Lab of Politecnico di Torino.
Version: 2021-03-03
Maintainer: Riccardo Novo (riccardo.novo@polito.it)
"""

from __future__ import division
import sys
import os
functions_folder = 'Functions'
scenario_configurator_folder = 'Scenario_configurator'
data_folder = 'Data'
sys.path.insert(1, functions_folder)
sys.path.insert(1, scenario_configurator_folder)
sys.path.insert(1, data_folder)
from input_dat_generation import dat_generation
from osemosys import osemosys_model
from pyomo.opt import SolverStatus, TerminationCondition


# %% USER CHOICES

# Choose the solver to be used (e.g. 'glpk', 'cplex', etc.), within those installed on your PC
solver = 'cplex'

# Choose whether you want to generate the input dat file from excel workbooks in scenario_configuration or not
# 'Yes' = generate .dat file; 'No' = .dat file already present
datgen = 'Yes'


# %% FILES PATHS

# Define some file paths
file_sets = os.path.join(scenario_configurator_folder, "1_SETS.xlsx")
file_parameters = os.path.join(scenario_configurator_folder, "2_PARAMETERS.xlsx")
file_dat = os.path.join(data_folder, "Input.dat")
file_json = os.path.join(data_folder, "results.json")


# %% GENERATION OF THE .dat INPUT FILE

if datgen == 'Yes':
    # Execute the dat_generation function to generate a dat input file from the excel
    # workbooks in scenario_configurator folder
    dat_generation(file_sets, file_parameters, file_dat)
    
    # Print to the console
    print("Input .dat file has been generated")


# %% BUILD AND SOLVE THE OSeMOSYS MODEL

# Execute the osemosys_model function and execute the model
model, instance, results = osemosys_model(file_dat, file_json, solver)

# Print to the console
print("Model has been built and solved")

# Print to the console the status if not successfull
if (results.solver.status != SolverStatus.ok) or (results.solver.termination_condition != TerminationCondition.optimal):
    # Do something when the solution in non optimal or infeasible
    print("Solver status : ", results.solver.status)
    print("Termination condition : ", results.solver.termination_condition)
    print("Quitting the execution")
    sys.exit()
