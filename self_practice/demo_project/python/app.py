import rename_data
import fetching_data
import sql_connection

json_data = rename_data.get_table_column_names()

ORIGINAL_FILENAMES = [f"t{i}" for i in json_data.keys()][:-3]
HUMAN_READABLE_FILENAMES = [json_data[i[1:]]["table"] for i in ORIGINAL_FILENAMES]


def main():
    while True:
        try:
            input_data = int(input("\nEnter 1 to fetch data, 2 to rename data, 3 to save to SQL Server and 0 to exit: \n>>> "))

            if input_data == 1:
                fetching_data.fetch_files(ORIGINAL_FILENAMES)
                print("Data fetched successfully.")

            elif input_data == 2:
                rename_data.rename_files(ORIGINAL_FILENAMES, HUMAN_READABLE_FILENAMES)
                print("Data renamed successfully.")

            elif input_data == 3:
                res = sql_connection.save_to_sql_server(HUMAN_READABLE_FILENAMES)
                if res:
                    print(res)
            elif input_data == 0:
                print("Exiting the program.")
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()