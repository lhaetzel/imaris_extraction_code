import os
import csv
import pandas as pd

#generate list of folders in directory (one folder per cell analyzed)
path= r'/Users/lhaetzel/Documents/Imaris_Statistics'
folder_list = os.listdir(path)
folder_list.remove('.DS_Store') 

#loop over each cell analyzed and calculate average spine length
Results = []
for i in range(len(folder_list)):
    #generate path to statistics folder for cell of interest
    cell_statistics = path + '/' + folder_list[i]
    
    #read csv file
    Spine_Part_Length_path = os.path.abspath(os.path.join(cell_statistics, 'Spine_Part_Length.csv'))
    row_list = []
    with open(Spine_Part_Length_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row_list.append(row)
    
    #fix formating errors 
    reformat_row_list = []
    for sublist in row_list:
        if len(sublist) == 12: #removes random empty lists that result from conversion
            reformat_row_list.append(sublist)
    
    #delete column headers
    reformat_row_list.remove(reformat_row_list[0])

    #extract the ground lengths and save them into a list
    Spine_Ground_Length_List = []
    for sublist in reformat_row_list:
        spine_ground_length = float(sublist[0])
        Spine_Ground_Length_List.append(spine_ground_length)
    
    #extract the head lengths and save them into a list
    Spine_Head_Length_List = []
    for sublist in reformat_row_list:
        spine_head_length = float(sublist[1])
        Spine_Head_Length_List.append(spine_head_length)

    #extract the neck lengths and save them into a list
    Spine_Neck_Length_List = []
    for sublist in reformat_row_list:
        spine_neck_length = float(sublist[2])
        Spine_Neck_Length_List.append(spine_neck_length)

    #calculate average ground, head and neck spine length, attribute it to cell number and append to results list
    Avg_Spine_Ground_Length = sum(Spine_Ground_Length_List)/len(Spine_Ground_Length_List)
    Avg_Spine_Head_Length = sum(Spine_Head_Length_List)/len(Spine_Head_Length_List)
    Avg_Spine_Neck_Length = sum(Spine_Neck_Length_List)/len(Spine_Neck_Length_List)

    #format output
    Output= [folder_list[i][1:-11], Avg_Spine_Ground_Length, Avg_Spine_Head_Length, Avg_Spine_Neck_Length] #folder list indexed so cell number appears as number
    Results.append(Output)

#convert into dataframe and export to excel
Spine_Part_Length_df=pd.DataFrame(Results)
Spine_Part_Length_df.columns = ['Cell Number', 'Spine Part Length Ground', 'Spine Part Length Head', 'Spine Part Length Neck']
Spine_Part_Length_df.to_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Spine_Part_Length.xlsx', index = False)
