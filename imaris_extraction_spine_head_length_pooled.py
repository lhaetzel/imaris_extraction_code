#head lengths pooled by genotype to make histogram

import os
import csv
import pandas as pd

#generate list of cells by genotype from key. have to remove nans and convert all values to strings
genotype_cell_key = pd.read_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/spine_analysis_cell_number_key.xlsx', sheet_name='cell_list')

HETD2_neg_Intake = genotype_cell_key['HETD2-'].tolist()
HETD2_pos_Intake = genotype_cell_key['HETD2+'].tolist()
WTD2_neg_Intake = genotype_cell_key['WTD2-'].tolist()
WTD2_pos_Intake = genotype_cell_key['WTD2+'].tolist()

#get rid of NaN
HETD2_neg_Clean = [x for x in HETD2_neg_Intake if str(x) != 'nan']
HETD2_pos_Clean = [x for x in HETD2_pos_Intake if str(x) != 'nan']
WTD2_neg_Clean = [x for x in WTD2_neg_Intake if str(x) != 'nan']
WTD2_pos_Clean = [x for x in WTD2_pos_Intake if str(x) != 'nan']

#get rid of decimal points

HETD2_neg_Clean_rounded = [round(elem) for elem in HETD2_neg_Clean]
HETD2_pos_Clean_rounded = [round(elem) for elem in HETD2_pos_Clean]
WTD2_neg_Clean_rounded = [round(elem) for elem in WTD2_neg_Clean]
WTD2_pos_Clean_rounded = [round(elem) for elem in WTD2_pos_Clean]

#convert values into strings
HETD2_neg_string = map(str,(HETD2_neg_Clean_rounded))
HETD2_neg_List = list(HETD2_neg_string)
HETD2_pos_string = map(str,(HETD2_pos_Clean_rounded))
HETD2_pos_List = list(HETD2_pos_string)
WTD2_neg_string = map(str,(WTD2_neg_Clean_rounded))
WTD2_neg_List = list(WTD2_neg_string)
WTD2_pos_string = map(str,(WTD2_pos_Clean_rounded))
WTD2_pos_List = list(WTD2_pos_string)


#now, we move to the imaris results
#loop over each cell analyzed and sort recorded head lengths into lists
#initialize lists
HETD2_neg_Results = []
HETD2_pos_Results = []
WTD2_neg_Results = []
WTD2_pos_Results = []

#generate list of folders in directory (one folder per cell analyzed)
path= r'/Users/lhaetzel/Documents/Imaris_Statistics'
folder_list = os.listdir(path)
folder_list.remove('.DS_Store') #sometimes this is not needed

for i in range(len(folder_list)):
    #generate path to statistics folder for cell of interest
    cell_statistics = path + '/' + folder_list[i]
    
    #read csv file
    Spine_Part_Mean_Length_path = os.path.abspath(os.path.join(cell_statistics, 'Spine_Part_Length.csv'))
    row_list = []
    with open(Spine_Part_Mean_Length_path) as csvfile:
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

    #extract the head lengths and save them into a list
    Spine_Head_Length_List = []
    for sublist in reformat_row_list:
        spine_head_length = float(sublist[1])
        Spine_Head_Length_List.append(spine_head_length)
    
    print(folder_list[i][1:-11])

    #sort values into correct list by genotype using cell number in folder name
    if folder_list[i][1:-11] in HETD2_neg_List:
        HETD2_neg_Results.extend(Spine_Head_Length_List)
        
    
    elif folder_list[i][1:-11] in HETD2_pos_List:
        HETD2_pos_Results.extend(Spine_Head_Length_List)
       

    elif folder_list[i][1:-11] in WTD2_neg_List:
        WTD2_neg_Results.extend(Spine_Head_Length_List)
        

    elif folder_list[i][1:-11] in WTD2_pos_List:
        WTD2_pos_Results.extend(Spine_Head_Length_List)
        

#convert to dataframe, add NaN where lists have different lengths, export to excel
Results_df = pd.DataFrame({'HETD2-': pd.Series(HETD2_neg_Results), 'HETD2+': pd.Series(HETD2_pos_Results), 'WTD2-': pd.Series(WTD2_neg_Results), 'WTD2+' : pd.Series(WTD2_pos_Results)})
Results_df.to_excel(r'/Users/lhaetzel/Desktop/Grad School/Rotations/Bateup Lab/Imaris_Export/Spine_Part_Head_Length_pooledbygenotype.xlsx', index = False)
    



  