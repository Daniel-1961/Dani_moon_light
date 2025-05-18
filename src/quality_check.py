import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    data = pd.read_csv(file_path, encoding='utf-8')
    
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    return data

def check_data_quality(data, columns):
    print(f"Data Quality Check for columns: {columns}\n")

    print("Missing values per column:")
    print(data[columns].isnull().sum(), "\n")


    for col in columns:
        invalid_values = data[(data[col] < -20) | (data[col] > 100) ]
        print(f"Invalid values in {col} (outside -20°C to 100°C):")
        print(invalid_values[[col]], "\n")

    if len(columns) > 1:
        correlation = data[columns[0]].corr(data[columns[1]])
        print(f"Correlation between {columns[0]} and {columns[1]}: {correlation:.2f}\n")

    data[columns].boxplot()
    plt.title(f"Boxplot of TModA and TModB {sample_space[i]}")
    plt.ylabel("Temperature (°C)")
    plt.show()

    if 'Timestamp' in data.columns:
        data.set_index('Timestamp', inplace=True)
        data[columns].plot(figsize=(12, 6))
        plt.title(f"TModA and TModB Over Time of {sample_space[i]}")
        plt.ylabel("Temperature (°C)")
        plt.xlabel("Time")
        plt.show()

def handle_missing_and_invalid(data, columns):
    for col in columns:
        data[col] = data[col].apply(lambda x: np.nan if x < -20 or x > 100 else x)

        data[col].fillna(data[col].mean(), inplace=True)
    
    print("\nMissing and invalid values handled.")
    return data

if __name__ == "__main__":
    sample_space = ['togo-dapaong', 'benin-malanville', 'sierraleone-bumbuna']

    file_list = ['togo-dapaong_qc.csv', 'benin-malanville.csv', 'sierraleone-bumbuna.csv']
    for i in range(3):
        file_path = file_list[i] 

        data = load_data(file_path)

        columns_to_check = ['TModA', 'TModB']

        check_data_quality(data, columns_to_check)
        
        data = handle_missing_and_invalid(data, columns_to_check)
