import duckdb
import datetime

# Example file path
INPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'
OUTPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\outbox\\'

# Generate a timestamp for the CSV file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# -----------------------------------------------------------------------------------

def SQL_COMPONENTS(query):
    # Find the position of the 'FROM' keyword
    KEYWORD_FROM = query.upper().find(" FROM ") + len(" FROM ")
    CLAUSE_SELECT = query[:KEYWORD_FROM]
    TABLE_NAME = query[KEYWORD_FROM:].split()[0]

    # Find the position of the 'WHERE' keyword, if it exists
    KEYWORD_WHERE = query.upper().find(" WHERE ")

    if KEYWORD_WHERE != -1:
        # Extract the WHERE clause if it exists
        CLAUSE_WHERE = " WHERE " + query[KEYWORD_WHERE + len(" WHERE "):]
    else:
        CLAUSE_WHERE = ""  # No WHERE clause

    return CLAUSE_SELECT, TABLE_NAME, CLAUSE_WHERE

# -----------------------------------------------------------------------------------


# Get the SQL query from the user (multi-line input)
SQL_QUERY = ""
print("Enter the SQL query (press Enter twice to finish):")
while True:
    line = input()
    if line == "":
        break  # Exit the loop if an empty line is entered
    SQL_QUERY += line + " "  # Concatenate the lines with a space

# Extract components from the SQL query
CLAUSE_SELECT, TABLE_NAME, CLAUSE_WHERE = SQL_COMPONENTS(SQL_QUERY)

# Build the file path for the table in the CSV format
TABLE_NAME_CSV = "'" + INPUT_FILE_PATH + TABLE_NAME + ".csv" + "'"

# Construct the query to run in DuckDB
SQL_QUERY_DB = CLAUSE_SELECT + TABLE_NAME_CSV + CLAUSE_WHERE

# -----------------------------------------------------------------------------------

# Execute the query in DuckDB
result = duckdb.sql(SQL_QUERY_DB)

print(result)

# -----------------------------------------------------------------------------------

# Create the CSV filename with the timestamp and table name
OUTPUT_FILE = f"{OUTPUT_FILE_PATH}{timestamp}_{TABLE_NAME}.csv"

# Save the result to a CSV file
result.to_csv(OUTPUT_FILE)

# Print confirmation
print(f"Query result saved to: {OUTPUT_FILE}")
