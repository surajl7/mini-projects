"""
AUTHOR: SURAJ A L
CREATED DATA: 2024-09-12
"""
# -----------------------------------------------------------------------------------

import duckdb
import datetime

# Example file paths
INPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'
OUTPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\outbox\\'

# Generate a timestamp for the CSV file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

WITH_HEADER = False
TEXT_QUALIFIER = '"'

# -----------------------------------------------------------------------------------

def SQL_COMPONENTS(query):
    # Find the position of the 'FROM' keyword
    KEYWORD_FROM = query.upper().find(" FROM ") + len(" FROM ")

    # Extract the SELECT part up to the FROM keyword
    CLAUSE_SELECT = query[:KEYWORD_FROM]

    # Extract everything after the FROM keyword (table names, joins, filters, etc.)
    FILTER_QUERY = query[KEYWORD_FROM:].strip().replace(";", "")

    # Tokenize the query to split into individual components
    QUERY_COMPONENTS = FILTER_QUERY.split()

    # Find the first occurrence of the table name (assumes the first non-keyword is the table)
    INPUT_FILE_NAME = QUERY_COMPONENTS[0]

    # Attach the file path to the table name for both the main table and join if any
    TABLE_NAME = f"'{INPUT_FILE_PATH}{INPUT_FILE_NAME}.csv'"


    # Now process the rest of the query to replace only the table names (not aliases)
    for i, token in enumerate(QUERY_COMPONENTS):
        if token == INPUT_FILE_NAME:
            QUERY_COMPONENTS[i] = TABLE_NAME


    # Reconstruct the remaining part of the query
    FINAL_QUERY = ' '.join(QUERY_COMPONENTS)

    return CLAUSE_SELECT, INPUT_FILE_NAME, FINAL_QUERY

# -----------------------------------------------------------------------------------

# Get the SQL query from the user (multi-line input)
SQL_QUERY = ""
print("Enter the SQL query (End's with semicolon):")
while True:
    line = input()
    SQL_QUERY += line + " "  # Concatenate the lines with a space
    if ";" in line:
        break  # Exit the loop if a semicolon is found

# Extract components from the SQL query
CLAUSE_SELECT, INPUT_FILE_NAME, FINAL_QUERY = SQL_COMPONENTS(SQL_QUERY)

# Construct the query to run in DuckDB
SQL_QUERY_DB = CLAUSE_SELECT + FINAL_QUERY

# print(SQL_QUERY_DB)

print("\n"+f"-"*100)
print("Executing query:")
print(SQL_QUERY_DB + ";")
print(f"-"*100+"\n")

# -----------------------------------------------------------------------------------

# Execute the query in DuckDB
result = duckdb.sql(SQL_QUERY_DB)
result_df = result.df()

print(result)

# -----------------------------------------------------------------------------------

# # Create the CSV filename with the timestamp and table name
# OUTPUT_FILE = f"{OUTPUT_FILE_PATH}{timestamp}_{INPUT_FILE_NAME}.csv"

# # Save the result to a CSV file
# result_df.to_csv(OUTPUT_FILE, index=False, quotechar=TEXT_QUALIFIER, quoting=1)

# print(f"Query result saved to: {OUTPUT_FILE}")
