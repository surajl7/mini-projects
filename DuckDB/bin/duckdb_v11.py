import duckdb
import datetime
import re

# Example file paths
INPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'
OUTPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\outbox\\'

# Generate a timestamp for the CSV file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

WITH_HEADER = False
TEXT_QUALIFIER = '"'

# -----------------------------------------------------------------------------------
def sql_components(query, input_file_path):
    """
    This function processes the SQL query, replaces multiple table names with file paths, 
    and returns the updated query components.
    """
    # Find the position of the 'FROM' keyword
    keyword_from = query.upper().find(" FROM ") + len(" FROM ")

    # Extract the SELECT part up to the FROM keyword
    clause_select = query[:keyword_from]

    # Extract everything after the FROM keyword (table names, joins, filters, etc.)
    filter_query = query[keyword_from:].strip().replace(";", "")

    # Regex to match table names, which can be aliased or unaliased
    table_pattern = r"([a-zA-Z_][a-zA-Z_0-9]*)(\s+[a-zA-Z_][a-zA-Z_0-9]*)?"

    # Find all table occurrences (supports multiple tables for joins)
    table_matches = re.findall(table_pattern, filter_query)

    # Dictionary to map table names to file paths
    table_file_mapping = {}

    for match in table_matches:
        table_name = match[0]  # First part is the table name
        alias = match[1].strip() if match[1] else ''  # Second part is the alias (optional)

        # Attach the file path to the table name
        table_file_mapping[table_name] = f"'{input_file_path}{table_name}.csv' {alias}".strip()

    # Replace table names in the filter_query with file paths
    for table_name, file_path in table_file_mapping.items():
        filter_query = re.sub(rf"\b{table_name}\b", file_path, filter_query)

    return clause_select, filter_query

# -----------------------------------------------------------------------------------
def execute_query(sql_query):
    """
    This function gets the SQL query from the user, executes it in DuckDB, and prints the result.
    """
    # Extract components from the SQL query
    clause_select, final_query = sql_components(sql_query, INPUT_FILE_PATH)

    # Construct the query to run in DuckDB
    sql_query_db = clause_select + final_query

    print("\n" + f"-" * 100)
    print("Executing query:")
    print(sql_query_db + ";")
    print(f"-" * 100 + "\n")

    # Execute the query in DuckDB
    result = duckdb.sql(sql_query_db)
    result_df = result.df()

    return result_df, sql_query_db

# -----------------------------------------------------------------------------------
def save_query_result(result_df, input_file_name):
    """
    This function saves the query result to a CSV file.
    """
    output_file = f"{OUTPUT_FILE_PATH}{timestamp}_{input_file_name}.csv"
    
    # Save the result to a CSV file
    result_df.to_csv(output_file, index=False, quotechar=TEXT_QUALIFIER, quoting=1)
    
    print(f"Query result saved to: {output_file}")

# -----------------------------------------------------------------------------------
def run_query_from_input():
    """
    This function accepts multi-line SQL input from the user and runs the query.
    """
    sql_query = ""
    print("Enter the SQL query (End's with semicolon):")
    while True:
        line = input()
        sql_query += line + " "  # Concatenate the lines with a space
        if ";" in line:
            break  # Exit the loop if a semicolon is found
    
    # Execute the query and return the result
    result_df, sql_query_db = execute_query(sql_query)

    # Print the result
    print(result_df)

    # Uncomment the following line if you want to save the result to a CSV file
    # save_query_result(result_df, 'query_result')



run_query_from_input()