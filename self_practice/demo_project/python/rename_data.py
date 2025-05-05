import os
import json
import pandas as pd


def rename_files(FILENAMES, cnt = 0):

    with open('../source/column_table_map.json', 'r') as file:
        table_column_names = json.load(file)


    for idx, name in enumerate(FILENAMES):
        ind = f"{idx+1:02d}"
        csv_path = f"../data/t{ind}.csv"
        
        if os.path.exists(csv_path):
            data = pd.read_csv(csv_path)
            column_names = table_column_names[ind]['columns'].values()  
            data.columns = column_names

            os.remove(f"../data/{name}.csv")
            data.to_csv(f"../data/{name}.csv", index=False)
            os.remove(csv_path)

            cnt += 1
            if cnt == 6:
                return True

        else:
            continue
