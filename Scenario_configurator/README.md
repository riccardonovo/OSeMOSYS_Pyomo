# OSeMOSYS Pyomo + scenario configurator

This extra tool simplifies the overall process for generating inputs to OSeMOSYS-Pyomo and enables the straightforward generation of a batch of scenarios.

The Python packages needed for using the scenario configurator are: Pyomo, Pandas, openpyxl


## 1 - Requirements
In addition to the general requirements for using OSeMOSYS-Pyomo, the Python packages needed for executing the process are: Pyomo, Pandas, Openpyxl.


## 2 - Defining SETS
In order to define the model SETS, you can open the "SETS.xlsx" workbook and complete the columns in the "Sets" sheet.


## 3 - Defining PARAMETERS
Close the "SETS.xlsx" and "PARAMETERS.xlsx" workbooks. To generate the correct PARAMETERS workbook, you should run the "parameters_workbook_generation.py". This will update the "PARAMETERS.xlsx" workbook.


## 4 - Generating the .dat input file and running the model solver
In order to launch the optimization, open "main.py", check the file paths and select the correct solver (e.g. GLPK). Run the code, and wait for the resolution. Inputs will be saved in the file_dat path as a .dat file, while results will be exported in the file_json path as a .json file, that can be easily processed by Python.


## Additional info
The tool can be exploited for generating several different scenarios: copy the SETS and PARAMETERS files in different folders, compile the PARAMETERS workbook and repeat steps 3 and 4 for every scenario). Also, the "main.py" code can be expanded in order to directly optimize the whole batch of scenarios and compare the outcomes.
