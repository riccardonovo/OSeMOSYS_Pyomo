""" 
Script developed @ the Energy Center Lab of Politecnico di Torino.
Version: 2021-03-03
Maintainer: Riccardo Novo (riccardo.novo@polito.it)
"""

# This code permits to create a .dat input file for OSeMOSYS-Pyomo starting from sets and parameters that were
# contained in xlsx files

import pandas as pd
import os
import timeit

def dat_generation(file_sets, file_parameters, file_dat):
        
    ### OPENING THE .txt FILE AND WRITING HEADER
    # If the file already exists, this section deletes it and re-creates it. Otherwise, it only creates a new file
    # file_dat = r'D:\Dati\PycharmProjects\OSeMOSYS_Pantelleria\Data\Pantelleria_Base\Input.dat'
    f_dat = open(file_dat, 'w')
    f_dat.write('# OSeMOSYS Pantelleria input file\n\n\n')
    
    ### READING THE SETS EXCEL FILE
    # This section reads the existing "1 - Sets.xlsx" excel file, where the physical structure of the model is defined
    # file_sets = r'D:\Dati\PycharmProjects\OSeMOSYS_Pantelleria\Data\Pantelleria_Base\1 - Sets.xlsx'
    df_sets = pd.read_excel(file_sets, 'Sets', header=0,
                            keep_default_na='True', dtype='str')
    
    ### READING THE INDEX SHEET OF THE PARAMETERS EXCEL FILE
    # file_parameters = r'D:\Dati\PycharmProjects\OSeMOSYS_Pantelleria\Data\Pantelleria_Base\2 - Parameters.xlsx'
    df_par = pd.read_excel(file_parameters, 'Index')
    
    ### WRITING THE SETS FOR THE .dat FILE
    f_dat.write('###############\n#    Sets     #\n###############\n\n')
    for col in df_sets.columns:
        if not df_sets[col].isnull().all():
            str = 'set ' + col + ' :=\n'
            f_dat.write(str)
            text = df_sets[col].dropna().tolist()
            f_dat.write('\n'.join(text))
            f_dat.write('\n  ;\n\n')
    
    ### WRITING THE PARAMETERS FOR THE .dat FILE WHILE READING THE PARAMETERS EXCEL FILE
    f_dat.write('####################\n#    Parameters     #\n####################\n\n')
    for index, row in df_par.iterrows():  # for loop over the list of input parameters
        dfp = pd.read_excel(file_parameters, row['Short name'],
                            dtype='str')  # reads the excel sheet named with the short name at the first page
        dfp = dfp[dfp['Value'].astype(float) != df_par.loc[index,'Default value']] # drops all default values
        dfp.reset_index(drop=True, inplace=True) # re-index the filtered dataframe
        if not dfp.empty:
            str = 'param ' + df_par.loc[index, 'Full name'] + ':=\n'
            f_dat.write(str)
            n_sets = sum(pd.notnull(df_par.iloc[index, 5:]).tolist())  # calculate the number of SETS for that parameter            
            if n_sets == 5:
                for index_par, row_par in dfp.iterrows():  # for loop over the sheet of the current parameter
                    f_dat.write(dfp.iloc[index_par, 0] + '\t' +
                                dfp.iloc[index_par, 1] + '\t' +
                                dfp.iloc[index_par, 2] + '\t' +
                                dfp.iloc[index_par, 3] + '\t' +
                                dfp.iloc[index_par, 4] + '\t' +
                                dfp.iloc[index_par, 5] + '\n')
            if n_sets == 4:
                for index_par, row_par in dfp.iterrows():  # for loop over the sheet of the current parameter
                    f_dat.write(dfp.iloc[index_par, 0] + '\t' +
                                dfp.iloc[index_par, 1] + '\t' +
                                dfp.iloc[index_par, 2] + '\t' +
                                dfp.iloc[index_par, 3] + '\t' +
                                dfp.iloc[index_par, 4] + '\n')
            if n_sets == 3:
                for index_par, row_par in dfp.iterrows():  # for loop over the sheet of the current parameter
                    f_dat.write(dfp.iloc[index_par, 0] + '\t' +
                                dfp.iloc[index_par, 1] + '\t' +
                                dfp.iloc[index_par, 2] + '\t' +
                                dfp.iloc[index_par, 3] + '\n')
            if n_sets == 2:
                for index_par, row_par in dfp.iterrows():  # for loop over the sheet of the current parameter
                    f_dat.write(dfp.iloc[index_par, 0] + '\t' +
                                dfp.iloc[index_par, 1] + '\t' +
                                dfp.iloc[index_par, 2] + '\n')
            if n_sets == 1:
                for index_par, row_par in dfp.iterrows():  # for loop over the sheet of the current parameter
                    f_dat.write(dfp.iloc[index_par, 0] + '\t' +
                                dfp.iloc[index_par, 1] + '\n')
            f_dat.write(';\n\n')
    
    # ### CLOSING THE FILE
    f_dat.close()
    print('End of the input .dat generation')
    return None

if __name__ == "__main__":
    path_parent = os.path.dirname(os.getcwd())
    scenconf_folder = os.path.join(path_parent,'Scenario_configurator')
    data_folder = os.path.join(path_parent,'Data')
    file_sets = os.path.join(scenconf_folder, "1_SETS.xlsx")
    file_parameters = os.path.join(scenconf_folder, "2_PARAMETERS.xlsx")
    file_dat = os.path.join(data_folder, "Input.dat")
    dat_generation(file_sets, file_parameters, file_dat)
