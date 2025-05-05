import pandas as pd
from environs import Env
from datetime import datetime
from logging_ import compare_and_log_changes 


# Load environment variables from .env file
env = Env()
env.read_env("../source/.env")

USER = env("USER")
REPO = env("REPO")
BRANCH = env("BRANCH")
FILE_PATH = env("FILE_PATH")


def fetch_data(file_name: str) -> pd.DataFrame:
    try:
        url = f"https://raw.githubusercontent.com/{USER}/{REPO}/{BRANCH}/{FILE_PATH}/{file_name}.csv"
        df = pd.read_csv(url)
        df  = df.to_csv(f"../data/{file_name}.csv", index=False)
        compare_and_log_changes(file_name, df)
        return df
    except Exception as e:
         with open(f"../logs/{file_name}_log.txt", "a") as f:
            f.write(f"[{datetime.now()}]Failed to fetch or process: {str(e)}\n")


def fetch_files(file_names, cnt = 0) -> bool:
    for file_name in file_names:
        if cnt == 6:
            return True
        else:
            if fetch_data(file_name):
                cnt += 1
            