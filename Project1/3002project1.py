#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:02:40 2022

@author: teagannorrgard
"""

import pandas as pd
import json
import csv
import sqlite3
#%%
## First, I will injest a local file for my processor to use.

f_path = '/Users/teagannorrgard/Spring2022/DS3003/Data/fossil-fuel-co2-emissions-by-nation.csv'
## file path from my local computer

df = pd.read_csv(f_path)
df = df.rename(columns={"Solid Fuel": "Solid_Fuel", "Liquid Fuel": "Liquid_Fuel", "Gas Fuel": "Gas_Fuel",
                        "Gas Flaring": "Gas_Flaring", "Per Capita":"Per_Capita",
                        "Bunker fuels (Not in Total)":"Bunker_Fuels"})
## I renamed the columns to make them easier to call later (some of them had spaces)


#%%

## Next, I will allow a user to choose which data format they would like

## I used a while loop for the user input so that if the user does not select one of my options,
## it will ask them the question again instead of breaking

file_type = None
while file_type not in {'CSV', 'JSON', 'SQL'}:
    file_type = input("What file type would you like? (CSV, JSON, SQL)").upper()
    ## used .upper() so that it would accept "csv" and "CSV"

## now using if/else statements to decide what to do based on user input
if file_type == 'CSV':
    file = df
    ## since the data loaded was already in .csv format, my processor doesn't need to do anything
    print("csv")
    
    
elif file_type == 'JSON':
    path = f_path.replace('.csv', '.json')
    ## I am creating a new file path for the user. 
    ## the JSON file will be stored in the same directory and as the same name,
    ## but as a .json instead of a .csv
    
    csvfile = open(f_path, 'r')
    ## I am reopening the csv file, 
    ## and creating a new empty json file to write in
    jsonfile = open(path, 'w')
    
    fieldnames = ('Year', 'Country', 'Total', 'Solid_Fuel', 'Liquid_Fuel', 'Gas_Fuel', 
                  'Cement', 'Gas_Flaring', 'Per_Capita', 'Bunker_Fuels')
    ## these are the names of the columns from the csv file which will also be the 
    ## 'headers' in the json file
    
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')
    ## my processor is going through every row of the csv and inserting it into the json file
    
    
elif file_type == 'SQL':
    path_to_db = "/Users/teagannorrgard/sqlite/mydata.db"
    ## I am using a pre existing database to build my table from the CSV
    
    conn = sqlite3.connect(path_to_db)
    ## connecting to the mysql database and creating a cursor 
    cursor = conn.cursor()
    conn.commit()
    
    ## creating an empty table with header names and types
    ## I used 'create table if not exists' to catch any possible errors if this line was run multiple times.
    ## I also used executescript() so that it could run the next command in the same go.
    cursor.executescript('''
        DROP TABLE fossil_fuels;
		CREATE TABLE IF NOT EXISTS fossil_fuels (
            Year int,
            Country nvarchar(50),
            Total int,
            Solid_Fuel int,
            Liquid_Fuel int,
            Gas_Fuel int,
            Cement int,
            Gas_Flaring int,
            Per_Capita int, 
            Bunker_Fuels int
			)
               ''')
    
    ## my processor is going through each row of the csv, and inserting each 
    ## piece of the row into the corresponding column from the table
    for row in df.itertuples():
        cursor.execute('''
                    INSERT INTO fossil_fuels (Year, Country, Total, Solid_Fuel, 
                                              Liquid_Fuel, Gas_Fuel, Cement, Gas_Flaring,
                                              Per_Capita, Bunker_Fuels)
                    VALUES (?,?,?,?,?,?,?,?,?,?)
                    ''',
                    (row.Year, 
                    row.Country,
                    row.Total,
                    row.Solid_Fuel,
                    row.Liquid_Fuel,
                    row.Gas_Fuel,
                    row.Cement,
                    row.Gas_Flaring,
                    row.Per_Capita,
                    row.Bunker_Fuels
                    ))
    conn.commit()
    ## commiting and now the fossil_fuels table has been populated.
    

    
#%%

## Last I will give a brief summary of the data.

print("This dataset contains fossil fuel emissions by country by year")
print("Number of Observations: ", df.shape[0])
print("Number of Features: ", df.shape[1])


    
    
    
    
    
    
    
    
    
