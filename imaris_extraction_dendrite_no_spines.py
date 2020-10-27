import os
import csv
import pandas as pd

#generate list of folders in directory (one folder per cell analyzed)
path= r'/Users/lhaetzel/Documents/Imaris_Statistics'
folder_list = os.listdir(path)
#folder_list.remove('.DS_Store')  

#loop over each cell analyzed and calculate average spine length
Results = []
for i in range(len(folder_list)):
    #generate path to statistics folder for cell of interest
    cell_statistics = path + '/' + folder_list[i]

#read csv file
    Spine_Number_path = os.path.abspath(os.path.join(cell_statistics, 'Dendrite_No._Spines.csv'))
    row_list = []
    with open(Spine_Number_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row_list.append(row)
    
    #fix formating errors 
    reformat_row_list = []
    for sublist in row_list:
        if len(sublist) == 9: #removes random empty lists that result from conversion
            reformat_row_list.append(sublist)
    
    #delete column headers
    reformat_row_list.remove(reformat_row_list[0])

    Spine_Number = reformat_row_list[0][0]
    Output= [folder_list[i][1:-11], Spine_Number] #folder list indexed so cell number appears as number
    Results.append(Output)

    #convert to excel spreadsheet via pandas dataframe and save
Dendrite_No_Spines_df=pd.DataFrame(Results)
Dendrite_No_Spines_df.columns = ['Cell Number', 'Spine Number']
Dendrite_No_Spines_df.to_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Dendrite_No._Spines.xlsx', index = False)