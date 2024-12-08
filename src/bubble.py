import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load the dataset from the specified file.

    :param file_path: Path to the dataset file.
    :return: DataFrame with parsed Timestamp column.
    """
    data = pd.read_csv(file_path, encoding='utf-8')
    
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    return data

def bubble_chart(data, x_column, y_column, size_column, color_column=None):
    """
    Create a bubble chart to visualize the relationship between x, y, and bubble size.

    :param data: DataFrame containing the data.
    :param x_column: Column name for the x-axis values.
    :param y_column: Column name for the y-axis values.
    :param size_column: Column name for the bubble size.
    :param color_column: Optional column name for bubble colors.
    """
    plt.figure(figsize=(10, 6))
    
    if color_column:
        scatter = plt.scatter(
            data[x_column], data[y_column], 
            s=data[size_column] * 10, 
            c=data[color_column], 
            cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5
        )
        plt.colorbar(scatter, label=color_column)
    else:
        plt.scatter(
            data[x_column], data[y_column], 
            s=data[size_column] * 10, 
            alpha=0.6, edgecolors="w", linewidth=0.5
        )

    plt.title("Bubble Chart")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ample_space = ['togo-dapaong', 'benin-malanville', 'sierraleone-bumbuna']

    file_list = ['togo-dapaong_qc.csv', 'benin-malanville.csv', 'sierraleone-bumbuna.csv']
    for i in range(3):    
        file_path = file_list[i]

        data = load_data(file_path)

        x_column = 'GHI'  
        y_column = 'DNI'  
        size_column = 'DHI'  
        color_column = 'Tamb'  

        bubble_chart(data, x_column, y_column, size_column, color_column)
