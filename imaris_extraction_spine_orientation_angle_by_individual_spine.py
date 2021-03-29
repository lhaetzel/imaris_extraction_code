#set up to be run in jupyter notebook or python interactive terminal. collects all of the individual spine lengths from imaris and compiles them into an excel sheet, with corresponding spine ID, animal number, cell number and genotype

import os
import csv
import pandas as pd

#generate list of folders in directory (one folder per cell analyzed)
path= r'/Users/lhaetzel/Documents/Imaris_Statistics'
folder_list = os.listdir(path)
folder_list.remove('.DS_Store')

#read in key for genotype, cell and animal number
genotype_cell_key_df = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/spine_analysis_cell_number_key.xlsx', sheet_name='Sheet1')

#initalize data frame
Master_df = pd.DataFrame(columns = ['Spine Orientation Angle', 'ID', 'cell number', 'animal number','genotype'])

#loop over all folders
for i in range(len(folder_list)):

    #specify folder path
    cell_statistics = path + '/' + folder_list[i]
    
    #read csv file
    Spine_Orientation_Angle_path = os.path.abspath(os.path.join(cell_statistics, 'Spine_Orientation_Angle.csv'))
    
    row_list = []
    with open(Spine_Orientation_Angle_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row_list.append(row)

    #fix formating errors 
    reformat_row_list = []
    for sublist in row_list:
        if len(sublist) == 9: #removes random empty lists that result from conversion
            reformat_row_list.append(sublist)
    
    #delete empty string at end of row
    for item in reformat_row_list:
        item.remove(item[-1])
    
    #convert csv into dataframe, add cell number
    Spine_Orientation_Angle_df = pd.DataFrame(reformat_row_list[1:])
    Spine_Orientation_Angle_df.columns = reformat_row_list[0]
    Spine_Orientation_Angle_df['cell number'] = folder_list[i][1:-11]

    #find corresponding animal number and genotype and add to dataframe
    cell_index_list = genotype_cell_key_df.index[genotype_cell_key_df['image_number'] == int(folder_list[i][1:-11])].tolist()
    cell_index = cell_index_list[0]
    animal_number = genotype_cell_key_df['animal_number'][cell_index]
    genotype = genotype_cell_key_df['genotype'][cell_index]

    #add animal number and genotype to dataframe

    Spine_Orientation_Angle_df['animal number'] = animal_number
    Spine_Orientation_Angle_df['genotype'] = genotype

    #delete irrelevant columns from dataframe
    Spine_Orientation_Angle_df = Spine_Orientation_Angle_df.drop(columns = ['Unit', 'Category', 'Depth', 'Level', 'Time', 'FilamentID'])

    #append to big dataframe
    Master_df = Master_df.append(Spine_Orientation_Angle_df)


#export to excel
Master_df.to_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Spine_Orientation_Angle_by_individual_spines.xlsx', index = False)
