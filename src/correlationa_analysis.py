import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
ind = 0

def correlation_analysis_with_line_graphs(data, columns):
    """
    Perform correlation analysis with a heatmap and line graphs for selected pairs of columns.

    :param data: DataFrame containing the data.
    :param columns: List of columns to include in the correlation analysis.
    """
    correlation_matrix = data[columns].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(f"Correlation Heatmap of {sample_space[ind]}")
    plt.show()

    print("\nVisualizing Line Graphs for Strongly Correlated Pairs (> 0.8)...")
    threshold = 0.8  
    strong_pairs = []

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            if abs(correlation_matrix.iloc[i, j]) > threshold:
                strong_pairs.append((columns[i], columns[j]))

    for col1, col2 in strong_pairs:
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data[col1], label=col1, alpha=0.7)
        plt.plot(data.index, data[col2], label=col2, alpha=0.7)
        plt.title(f"Line Graph: {col1} vs {col2} of {sample_space[ind]}")
        plt.xlabel("Time")
        plt.ylabel("Values")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
     
    sample_space = ['togo-dapaong', 'benin-malanville', 'sierraleone-bumbuna']

    file_list = ['togo-dapaong_qc.csv', 'benin-malanville.csv', 'sierraleone-bumbuna.csv']
    for i in range(3):
            file_path = file_list[i]  
            data = pd.read_csv(file_path, encoding='utf-8')

            if 'Timestamp' in data.columns:
                data['Timestamp'] = pd.to_datetime(data['Timestamp'])
                data.set_index('Timestamp', inplace=True)

            columns_to_analyze = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'TModA', 'TModB']

            correlation_analysis_with_line_graphs(data, columns_to_analyze)
            ind +=1
