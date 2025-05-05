import os
import pandas as pd
from sqlalchemy import text, create_engine


# SQL Server connection details
SERVER = "DESKTOP-L0MHKPI\\SQLEXPRESS"
DATABASE = 'demo_project'


# Use a trusted connection (Windows auth): "Trusted_Connection=yes"
connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    "&Trusted_Connection=yes"
)

def save_to_sql_server(FILENAMES: list):
    results = 0
    try:
        engine = create_engine(connection_string)
        for filename in FILENAMES:
            csv_path = f"../data/{filename}.csv"
            if os.path.exists(csv_path):
                data = pd.read_csv(csv_path)
                data.to_sql(filename, con=engine, if_exists='replace', index=False)
                print(f"File saved successfully: {filename}.csv")
                results += 1
            else:
                print(f"File not found: {csv_path}")
        return results

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"