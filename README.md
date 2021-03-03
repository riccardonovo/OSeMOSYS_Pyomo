# OSeMOSYS Pyomo

## Installation

To run OSeMOSYS Pyomo you need to install a few Python dependencies in a Python environment.

One of the easiest ways to install a Python environment is with
[miniconda](https://docs.conda.io/en/latest/miniconda.html).

After installing miniconda, run the following commands in your terminal window:

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -n pyomo python=3.8 pyomo glpk  # we install pyomo and the free GLPK solver
conda activate pyomo  # activate our Python environment called 'pyomo'
```

Alternatively to GLPK, you can also install the commercial solver CPLEX.


## Folders and files
The following files and folders are contained in the master folder:
- main.py script: main code for the solution of the OSeMOSYS model
- Data folder: folder containing the Input.dat input file and the results.json output file
- Functions folder: folder containing the input_dat_generation.py script and the
- Scenario_configurator folder: fodler containing the scenario configurator (see README_scenario_configurator.md)
- CHANGELOD.md: log file containing changes wrt. previous versions of OSeMOSYS
- README.md: current file


## Running you first model run

To run OSeMOSYS Python, open the main.py script, indicate the solver to be used and choose whether the Input.dat file must be generated from the excel workbooks in the Scenario_configurator or not. In case it is not, insert a suitable Input.dat file in the Data folder.
Run the script and see the results in the Data folder.

## Where to get help

If you need general help with OSeMOSYS, please submit posts on our friendly global
[forum](https://groups.google.com/forum/#!forum/osemosys) where there are many topics
and existing answers to other questions.

If you have identified a problem specific to OSeMOSYS Pyomo, please submit a new issue in the [issue tracker](https://github.com/OSeMOSYS/OSeMOSYS_Pyomo/issues/new).

If you have an idea or have identified a bug or problem which you think is relevant for the wider OSeMOSYS
community, please submit a [new issue](https://github.com/OSeMOSYS/OSeMOSYS/issues/new/choose) at the main OSeMOSYS repository.
