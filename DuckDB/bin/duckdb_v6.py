
import duckdb

FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'

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
        # Set CLAUSE_WHERE to an empty string if WHERE clause is not present
        CLAUSE_WHERE = ""

    return CLAUSE_SELECT, TABLE_NAME, CLAUSE_WHERE

# Example usage

# SQL_QUERY = input("Enter the query: \n")
# --------------------------------------------------------------------------
SQL_QUERY = ""
print("Enter the SQL query (press Enter twice to finish):")

while True:
    line = input()
    if line == "":
        break  # Exit the loop if an empty line is entered
    SQL_QUERY += line + " "  # Concatenate the lines with a space

# print(f"Your query is:\n{SQL_QUERY}")
# --------------------------------------------------------------------------

CLAUSE_SELECT, TABLE_NAME, CLAUSE_WHERE = SQL_COMPONENTS(SQL_QUERY)


TABLE_NAME_CSV = "'" + FILE_PATH + TABLE_NAME + ".csv" + "'"

# print(f"SELECT ITEMS: {CLAUSE_SELECT}")
# print(f"TABLE NAME: {TABLE_NAME}")
# print(f"WHERE CLAUSE: {CLAUSE_WHERE}")

SQL_QUERY_DB = CLAUSE_SELECT + TABLE_NAME_CSV + CLAUSE_WHERE

# print(SQL_QUERY_DB)

print(duckdb.sql(SQL_QUERY_DB))

