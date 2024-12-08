import pandas as pd
import numpy as np
import datetime

def load_data(data):
    '''loads the data into a DataFramme
        if the input is DataFrame, it returns it direcly
        If the input is a file path, it reads the file into a DataFrame'''
    if isinstance(data, pd.DataFrame):
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return data
    elif isinstance(data, str):
        df = pd.read_csv(data)  
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        print(df['Timestamp'].dtypes)


    else: 
        raise ValueError("input should be DataFrame or a file path(string).")

    
    return df

# Summary 
def get_summary_statistics(data):
    df = load_data(data)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    summary = df[numeric_cols].describe()
    return summary

sample_space = ['togo-dapaong', 'benin-malanville', 'sierraleone-bumbuna']

file_list = ['togo-dapaong_qc.csv', 'benin-malanville.csv', 'sierraleone-bumbuna.csv']
for i in range(3):
    print(get_summary_statistics(file_list[i]))
