import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load the dataset for temperature analysis.

    :param file_path: Path to the dataset file.
    :return: DataFrame with a parsed Timestamp column.
    """
    data = pd.read_csv(file_path, encoding='utf-8')
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    return data

def temperature_analysis(data, temperature_columns):
    """
    Perform temperature analysis by examining trends, distributions, and comparisons.

    :param data: DataFrame containing the data.
    :param temperature_columns: List of columns containing temperature data.
    """
    print("\nTemperature Analysis Summary:\n")
    print(data[temperature_columns].describe(), "\n")

    for column in temperature_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True, color='blue', bins=30)
        plt.title(f"Distribution of {column} of {sample_space[i]}")
        plt.xlabel("Temperature (°C)")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()

    if 'Timestamp' in data.columns:
        plt.figure(figsize=(12, 6))
        for column in temperature_columns:
            plt.plot(data['Timestamp'], data[column], label=column, alpha=0.7)
        plt.title(f"Temperature Trends Over Time of {sample_space[i]}")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.grid(True)
        plt.show()

    correlation_matrix = data[temperature_columns].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(f"Correlation Heatmap for Temperatures of {sample_space[i]}")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data[temperature_columns])
    plt.title(f"Temperature Variability of {sample_space[i]}")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    sample_space = ['togo-dapaong', 'benin-malanville', 'sierraleone-bumbuna']

    file_list = ['togo-dapaong_qc.csv', 'benin-malanville.csv', 'sierraleone-bumbuna.csv']
    for i in range(3):
        file_path = file_list[i]

        data = load_data(file_path)

        temperature_columns = ['Tamb', 'TModA', 'TModB'] 
        temperature_analysis(data, temperature_columns)
