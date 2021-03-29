import os
import csv
import pandas as pd

#generate list of folders in directory (one folder per filament analyzed)
path= r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/A2A - Statistics'
folder_list = os.listdir(path)
folder_list.remove('.DS_Store')

#initalize data frame
Master_df = pd.DataFrame(columns = [ 'Spine Part Mean Diameter Head', 'cell/filament number'])

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

    #find average head diameter
    Head_Diameter_List = Spine_Part_Diameter_df['Spine Part Mean Diameter Head'].tolist()
    Head_Diameter_List = list(map(float, Head_Diameter_List))
    Average_Head_Diameter = sum(Head_Diameter_List)/len(Head_Diameter_List)


    #define cell and filament id
    Cell_Fil_ID = folder_list[i]

    #format information such that it can be appended to master dataframe
    Summary_List = [Average_Head_Diameter, Cell_Fil_ID]
    Cell_df = pd.DataFrame([Summary_List], columns = [ 'Spine Part Mean Diameter Head', 'cell/filament number'])

    #append to big dataframe
    Master_df = Master_df.append(Cell_df)

#export to excel
Master_df.to_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/A2A_Head_Diameters.xlsx', index = False)
