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
    Spine_Length_path = os.path.abspath(os.path.join(cell_statistics, 'Spine_Length.csv'))
    row_list = []
    with open(Spine_Length_path) as csvfile:
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

    #extract the spine length values from csv file and convert ehm to floats
    Spine_Length_List = []
    for sublist in reformat_row_list:
        spine_length = float(sublist[0])
        Spine_Length_List.append(spine_length)

    #calculate average spine length, attribute it to cell number and append to results list
    Average_Spine_Length = sum(Spine_Length_List)/len(Spine_Length_List)
    Output= [folder_list[i][1:-11], Average_Spine_Length] #folder list indexed so cell number appears as number
    Results.append(Output)

#convert to excel spreadsheet via pandas dataframe and save
Spine_Length_df=pd.DataFrame(Results)
Spine_Length_df.columns = ['Cell Number', 'Spine Length Mean']
Spine_Length_df.to_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Spine_Length.xlsx', index = False)