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
Master_df = pd.DataFrame(columns = ['Spine Part Mean Diameter Head', 'ID', 'cell number', 'Spine Type', 'animal number','genotype'])

#loop over all folders
for i in range(len(folder_list)):

    #specify folder path
    cell_statistics = path + '/' + folder_list[i]
    
    #read csv file
    Spine_Diameter_path = os.path.abspath(os.path.join(cell_statistics, 'Spine_Part_Mean_Diameter.csv'))
    row_list = []
    with open(Spine_Diameter_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row_list.append(row)

    #fix formating errors 
    reformat_row_list = []
    for sublist in row_list:
        if len(sublist) == 12: #removes random empty lists that result from conversion
            reformat_row_list.append(sublist)
    for sublist in reformat_row_list:
        sublist.remove(sublist[-1])

    #convert csv into dataframe, add cell number
    Spine_Part_Diameter_df = pd.DataFrame(reformat_row_list[1:])
    Spine_Part_Diameter_df.columns = reformat_row_list[0]
    Spine_Part_Diameter_df['cell number'] = folder_list[i][1:-11]

    #find corresponding animal number and genotype and add to dataframe
    cell_index_list = genotype_cell_key_df.index[genotype_cell_key_df['image_number'] == int(folder_list[i][1:-11])].tolist()
    cell_index = cell_index_list[0]
    animal_number = genotype_cell_key_df['animal_number'][cell_index]
    genotype = genotype_cell_key_df['genotype'][cell_index]

    #add animal number and genotype to dataframe

    Spine_Part_Diameter_df['animal number'] = animal_number
    Spine_Part_Diameter_df['genotype'] = genotype

    #delete irrelevant columns from dataframe
    Spine_Part_Diameter_df = Spine_Part_Diameter_df.drop(columns = ['Spine Part Mean Diameter Ground','Spine Part Mean Diameter Neck','Unit', 'Category', 'Collection', 'Depth', 'Level', 'Time', 'FilamentID'])

    #append to big dataframe
    Master_df = Master_df.append(Spine_Part_Diameter_df)

#assign spine type by head diameter

for index in range(len(Master_df['Spine Part Mean Diameter Head'])):
    if float(Master_df['Spine Part Mean Diameter Head'].iloc[index]) <0.32:
        spine_type = 'filopodia'
    elif float(Master_df['Spine Part Mean Diameter Head'].iloc[index]) > 0.48:
        spine_type = 'mushroom'
    else:
        spine_type = 'stubby'
    Master_df['Spine Type'].iloc[index] = spine_type


#classify number of spine types per cell

Morphology_df = Master_df.drop(columns = ['ID', 'Spine Part Mean Diameter Head', 'animal number'])
Cell_Array = Morphology_df['cell number'].unique()

cell_morphology_master_list = []
for cell in Cell_Array:
    cell_morphology_list = [cell,[]]
    for value in range(len(Morphology_df['cell number'])):
        if Morphology_df['cell number'].iloc[value] == cell:
           cell_morphology_list[1].append(Morphology_df['Spine Type'].iloc[value])
    cell_morphology_master_list.append(cell_morphology_list)

#initialize data frame
Morphology_Master_df = pd.DataFrame(columns = ['cell number','mushroom','stubby', 'filopodia'])

for cell_list in cell_morphology_master_list:
    #add cell number
    Morphology_Master_df = Morphology_Master_df.append({'cell number': cell_list[0]}, ignore_index=True)
    index_cell = Morphology_Master_df.index[Morphology_Master_df['cell number'] == cell_list[0]].tolist()
    mushroom_count = cell_list[1].count('mushroom')
    stubby_count = cell_list[1].count('stubby')
    filopodia_count = cell_list[1].count('filopodia')

    Morphology_Master_df['mushroom'][index_cell] = mushroom_count
    Morphology_Master_df['stubby'][index_cell] = stubby_count
    Morphology_Master_df['filopodia'][index_cell] =filopodia_count



#export to excel
Morphology_Master_df.to_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Spine_Morphology_by_cell.xlsx', index = False)
