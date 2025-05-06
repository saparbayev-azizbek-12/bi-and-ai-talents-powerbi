import os
import json
import pandas as pd


def get_table_column_names(file_path="../source/column_table_map.json"):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def rename_files(ORIGINAL_FILENAMES, FILENAMES, cnt = 0):

    for ind, name in zip(ORIGINAL_FILENAMES, FILENAMES):
        csv_path = f"../data/{ind}.csv"
        
        if os.path.exists(csv_path):
            data = pd.read_csv(csv_path)
            table_column_names = get_table_column_names()
            column_names = table_column_names[ind[1:]]['columns'].values()  
            data.columns = column_names

            os.remove(f"../data/{name}.csv")
            data.to_csv(f"../data/{name}.csv", index=False)
            os.remove(csv_path)

            cnt += 1
            if cnt == 6:
                return True

        else:
            continue
