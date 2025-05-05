import pandas as pd
from datetime import datetime
import os

def compare_and_log_changes(file_name: str, new_df: pd.DataFrame):
    path_old = f"../data/{file_name}.csv"
    path_log = f"../logs/{file_name}_log.txt"
    
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    if not os.path.exists(path_old):
        new_df.to_csv(path_old, index=False)
        with open(path_log, "a") as f:
            f.write(f"{timestamp} Initial download. Rows: {len(new_df)}\n")
        return

    old_df = pd.read_csv(path_old)

    # Identify added, deleted, updated rows
    added = pd.concat([new_df, old_df]).drop_duplicates(keep=False)
    deleted = pd.concat([old_df, new_df]).drop_duplicates(keep=False)
    updated = new_df.merge(old_df, how='inner', indicator=False)
    updated = updated[~(new_df == old_df).all(axis=1)]  # just changed rows

    # Save new version
    new_df.to_csv(path_old, index=False)

    with open(path_log, "a", encoding='utf-8') as f:
        f.write(f"{timestamp} --- Update Summary ---\n")
        if not added.empty:
            f.write(f"Added {len(added)} row(s)\n")
        if not deleted.empty:
            f.write(f"Deleted {len(deleted)} row(s)\n")
        if not updated.empty:
            f.write(f"Updated {len(updated)} row(s)\n")
        if added.empty and deleted.empty and updated.empty:
            f.write("No changes detected\n")