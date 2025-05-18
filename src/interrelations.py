import pandas as pd
import matplotlib.pyplot as plt

def load_and_prepare_data(file_path, location_name):
    """
    Load and prepare the dataset for analysis.

    :param file_path: Path to the dataset file.
    :param location_name: Name of the location (used for labeling).
    :return: DataFrame with an additional 'Location' column.
    """
    data = pd.read_csv(file_path, encoding='utf-8')
    
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    data['Location'] = location_name
    return data

def compare_datasets_with_horizontal_lines(dataframes, columns):
    """
    Compare the specified columns across multiple datasets using horizontally arranged line graphs.

    :param dataframes: List of DataFrames to compare.
    :param columns: List of columns to analyze (e.g., ['GHI', 'DNI', 'DHI', 'Tamb']).
    """
    combined_data = pd.concat(dataframes, ignore_index=True)

    for column in columns:
        locations = combined_data['Location'].unique()
        num_locations = len(locations)
        
        fig, axes = plt.subplots(
            nrows=num_locations, ncols=1, figsize=(12, 6 * num_locations), sharex=True
        )
        fig.suptitle(f"Comparison of {column} Across Locations", fontsize=16)

        for ax, location in zip(axes, locations):
            location_data = combined_data[combined_data['Location'] == location]
            ax.plot(location_data['Timestamp'], location_data[column], label=location, alpha=0.8)
            ax.set_title(f"{location} - {column}")
            ax.set_xlabel("Time")
            ax.set_ylabel(column)
            ax.grid(True)
            ax.legend()

        plt.tight_layout(rect=[0, 0, 1, 0.97])
        plt.show()

# Main Function
if __name__ == "__main__":
    
    file_list = ['togo-dapaong_qc.csv', 'benin-malanville.csv', 'sierraleone-bumbuna.csv']

    file_path1 = file_list[1]
    file_path2 = file_list[2]
    file_path3 = file_list[0]

    data_benin = load_and_prepare_data(file_path1, "Benin")
    data_sierra_leone = load_and_prepare_data(file_path2, "Sierra Leone")
    data_togo = load_and_prepare_data(file_path3, "Togo")

    datasets = [data_benin, data_sierra_leone, data_togo]

    columns_to_analyze = ['GHI', 'DNI', 'DHI', 'Tamb']
    compare_datasets_with_horizontal_lines(datasets, columns_to_analyze)
