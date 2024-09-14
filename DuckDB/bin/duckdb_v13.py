"""
AUTHOR: SURAJ A L
CREATED DATA: 2024-09-14
"""
# -----------------------------------------------------------------------------------

import duckdb
import datetime

# INPUT_FILE_EXTENSION = '.csv'

INPUT_FILE_PATH      = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'
OUTPUT_FILE_PATH     = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\outbox\\'

WITH_HEADER          = True
WITH_INDEX           = False
TEXT_QUALIFIER       = '"'

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# -----------------------------------------------------------------------------------

def INPUT_FROM_USER():
    """
    This function accepts multi-line SQL input from the user.
    """

    SQL_QUERY = ""
    print("Enter the SQL query (End's with semicolon):")
    while True:
        line = input()
        SQL_QUERY += line + " " 
        if ";" in SQL_QUERY:
            break
    
    return SQL_QUERY

# -----------------------------------------------------------------------------------

# def SQL_COMPONENTS(SQL_QUERY_STRING, INPUT_FILE_PATH, INPUT_FILE_EXTENSION):
def SQL_COMPONENTS(SQL_QUERY_STRING, INPUT_FILE_PATH):
    """
    This function processes the SQL query, replaces multiple table names with file paths, 
    and returns the updated query components.
    """
    try:
        SQL_QUERY_STRING_LIST = SQL_QUERY_STRING.upper().strip().replace(";","").split()

        KEYWORD_LIST = ['FROM','JOIN']
        TABLE_NAME_LIST  = []

        for KEYWORD in KEYWORD_LIST:
            if KEYWORD in SQL_QUERY_STRING_LIST:
                indices = [i for i, x in enumerate(SQL_QUERY_STRING_LIST) if x == KEYWORD]
                # print(indices)
                for index in indices:
                    TABLE_NAME_INDEX = index + 1
                    if TABLE_NAME_INDEX < len(SQL_QUERY_STRING_LIST):
                        TABLE_NAME = SQL_QUERY_STRING_LIST[TABLE_NAME_INDEX]
                        TABLE_NAME_LIST.append(TABLE_NAME)
                        SQL_QUERY_STRING_LIST[TABLE_NAME_INDEX] = f"'{INPUT_FILE_PATH}{TABLE_NAME}.csv'"

        FINAL_QUERY = ' '.join(SQL_QUERY_STRING_LIST)

        return TABLE_NAME_LIST, FINAL_QUERY

    except:
        print("Error: Something wrong with input SQL Query")

# -----------------------------------------------------------------------------------

def SAVE_QUERY_RESULT(result_df, table_name, OUTPUT_FILE_PATH, WITH_INDEX=False, WITH_HEADER=True, TEXT_QUALIFIER=""):
    """
    This function saves the query result to a CSV file.
    """
    OUTPUT_FILE = f"{OUTPUT_FILE_PATH}{timestamp}_{table_name}.csv"
    
    # Save the result to a CSV file
    result_df.to_csv(OUTPUT_FILE, index=WITH_INDEX, header=WITH_HEADER, quotechar=TEXT_QUALIFIER, quoting=1)
    
    print(f"Query result saved to: {OUTPUT_FILE}")

# -----------------------------------------------------------------------------------

def EXECUTE_QUERY(INPUT_FILE_PATH, OUTPUT_FILE_PATH, SAVE_OUTPUT='NO'):
    """
    This function gets the SQL query from the user, executes it in DuckDB, and prints the result.
    """
    try:
        SQL_QUERY = INPUT_FROM_USER()

        TABLE_NAME_LIST, FINAL_QUERY = SQL_COMPONENTS(SQL_QUERY, INPUT_FILE_PATH)

        print("\n" + f"-" * 100)
        print(f"Executing query: \n{FINAL_QUERY};")
        print(f"-" * 100 + "\n")

        # Execute the query in DuckDB
        result = duckdb.sql(FINAL_QUERY)
        result_df = result.df()

        print(result)

        if SAVE_OUTPUT in ["YES", "Y", "yes", "y", "Yes"]:
            SAVE_QUERY_RESULT(result_df, TABLE_NAME_LIST[0], OUTPUT_FILE_PATH, WITH_INDEX=WITH_INDEX, WITH_HEADER=WITH_HEADER, TEXT_QUALIFIER=TEXT_QUALIFIER)

        return result_df, TABLE_NAME_LIST, FINAL_QUERY
    
    except duckdb.BinderException as e:
        print(f"ERROR: {e}")

# -----------------------------------------------------------------------------------


EXECUTE_QUERY(INPUT_FILE_PATH, OUTPUT_FILE_PATH, "Y")