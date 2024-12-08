import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='utf-8')

    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    data.set_index('Timestamp', inplace=True)
    return data

def time_series_analysis(data, columns):
    print(f"\nPerforming Time Series Analysis for columns: {columns}\n")

    plt.figure(figsize=(12, 6))
    for column in columns:
        if column in data.columns:
            plt.plot(data.index, data[column], label=column)

    plt.title(f"Time Series Analysis of {sample_space[i]}")
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.legend()
    plt.grid(True)
    plt.show()

    data['Month'] = data.index.month
    monthly_avg = data.groupby('Month')[columns].mean()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=monthly_avg, markers=True)
    plt.title(f"Monthly Average Trends of {sample_space[i]}")
    plt.xlabel("Month")
    plt.ylabel("Average Values")
    plt.legend(columns)
    plt.grid(True)
    plt.show()

    data['Hour'] = data.index.hour
    hourly_avg = data.groupby('Hour')[columns].mean()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=hourly_avg, markers=True)
    plt.title(f"Hourly Average Patterns of {sample_space[i]}")
    plt.xlabel("Hour")
    plt.ylabel("Average Values")
    plt.legend(columns)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    
    sample_space = ['togo-dapaong', 'benin-malanville', 'sierraleone-bumbuna']

    file_list = ['togo-dapaong_qc.csv', 'benin-malanville.csv', 'sierraleone-bumbuna.csv']
    for i in range(3):
        file_path = file_list[i]  
        data = load_data(file_path)
        columns_to_analyze = ['GHI', 'DNI', 'DHI', 'Tamb'] 
        time_series_analysis(data, columns_to_analyze)
