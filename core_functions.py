'''List of core functions - aim is to run only one file that outputs all desired parameters - this may not be possible'''

import os
import csv
import pandas as pd


def path_finder():
    '''asks the user for path'''
    path = input("Please input the path to your Imaris Statistics folder")
    return path

def folder_list_generator(path):
    '''takes the path and generates list of folders in that path'''
    folder_list = os.listdir(path)
    folder_list.remove('.DS_Store')
    return folder_list

def reformat_CSV_list(row_list):
    '''takes row_list and reformats it accordingly'''
    #fix formating errors 
    reformat_row_list = []
    for sublist in row_list:
        if len(sublist) == 9: #removes random empty lists that result from conversion, double check as sublist length may vary by parameter
            reformat_row_list.append(sublist)
    
        #delete column headers
    reformat_row_list.remove(reformat_row_list[0])

    return reformat_row_list

def spine_area_save_file(Results):
    '''saves dataframe as excel sheet to specified path'''
    #convert to excel spreadsheet via pandas dataframe and save
    Spine_Area_df=pd.DataFrame(Results)
    Spine_Area_df.columns = ['Cell Number', 'Spine Area Mean'] #will also vary by file
    save_path = input("Please specify the path where'd you'd like to save the files.")
    Spine_Area_df.to_excel(save_path, index = False)

    return "saved to" + save_path