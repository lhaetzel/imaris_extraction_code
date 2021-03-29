import os
import csv
import pandas as pd

def spine_area_extractor():
    '''uses below functions to extract spine areas'''

    path = path_finder()
    folder_list = folder_list_generator(path)
    row_list = CSV_extractor_spine_area(path, folder_list)
    reformat_row_list = reformat_CSV_list(row_list)

    Results = []
    #extract the spine Area values from csv file and convert them to floats
    Spine_Area_List = []
    for sublist in reformat_row_list:
        spine_area = float(sublist[0])
        Spine_Area_List.append(spine_area)
    
    #calculate average spine Area, attribute it to cell number and append to results list
    Average_Spine_Area = sum(Spine_Area_List)/len(Spine_Area_List)
    Output= [folder_list[i][1:-11], Average_Spine_Area] #folder list indexed so cell number appears as number
    Results.append(Output)
    
    return Results

def spine_area_save_file(Results):
    '''saves dataframe as excel sheet to specified path'''
    #convert to excel spreadsheet via pandas dataframe and save
    Spine_Area_df=pd.DataFrame(Results)
    Spine_Area_df.columns = ['Cell Number', 'Spine Area Mean']
    save_path = input("Please specify the path where'd you'd like to save the files.")
    Spine_Area_df.to_excel(save_path, index = False)

    return "saved to" + save_path

def path_finder():
    '''asks the user for path'''
    path = input("Please input the path to your Imaris Statistics folder")
    return path

def folder_list_generator(path):
    '''takes the path and generates list of folders in that path'''
    folder_list = os.listdir(path)
    folder_list.remove('.DS_Store')
    return folder_list

def CSV_extractor_spine_area(path, folder_list):
    '''Takes the specified path and generates a list of rows based on CSV files'''

    
    for i in range(len(folder_list)):
    #generate path to statistics folder for cell of interest
        cell_statistics = path + '/' + folder_list[i]

    #read csv file
    Spine_Area_path = os.path.abspath(os.path.join(cell_statistics, 'Spine_Area.csv'))
    row_list = []
    with open(Spine_Area_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row_list.append(row)
    
    return row_list

    def reformat_CSV_list(row_list):
        '''takes row_list and reformats it accordingly'''
        #fix formating errors 
        reformat_row_list = []
        for sublist in row_list:
            if len(sublist) == 9: #removes random empty lists that result from conversion
                reformat_row_list.append(sublist)
    
        #delete column headers
        reformat_row_list.remove(reformat_row_list[0])

        return reformat_row_list
