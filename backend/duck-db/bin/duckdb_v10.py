
import re

# Example file paths
INPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'
OUTPUT_FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\outbox\\'

# # Get the SQL query from the user (multi-line input)
# SQL_QUERY = ""
# print("Enter the SQL query (End's with semicolon):")
# while True:
#     line = input()
#     SQL_QUERY += line + " " 
#     if ";" in line:
#         break

SQL_QUERY = """
SELECT e1.employee_name, e2.employee_name 
FROM employee e1 
JOIN sample_data d ON e1.department_id = d.department_id;
"""

# print(SQL_QUERY)

KEYWORD_FROM = SQL_QUERY.upper().find("FROM") + len("FROM")

CLAUSE_SELECT = SQL_QUERY[:KEYWORD_FROM].strip()

FILTER_QUERY = SQL_QUERY[KEYWORD_FROM:].strip().replace(";", "")

QUERY_COMPONENTS = FILTER_QUERY.split()

INPUT_FILE_NAME = QUERY_COMPONENTS[0]

TABLE_NAME = f"'{INPUT_FILE_PATH}{INPUT_FILE_NAME}.csv'"



print(KEYWORD_FROM)
print(CLAUSE_SELECT)
print(FILTER_QUERY)
print(QUERY_COMPONENTS)
print(INPUT_FILE_NAME)
print(TABLE_NAME)



print()

table_pattern = r"([a-zA-Z_][a-zA-Z_0-9]*)(\s+[a-zA-Z_][a-zA-Z_0-9]*)?"

print(table_pattern)

table_matches = re.findall(table_pattern, FILTER_QUERY)

print(table_matches)

table_file_mapping = {}

print(table_file_mapping)

for match in table_matches:
    TABLE_NAME = match[0]
    print("TABLE_NAME: "+TABLE_NAME)
    alias = match[1].strip() if match[1] else ''
    # print("--")
    print("alias: " + alias)

    table_file_mapping[TABLE_NAME] = f"'{INPUT_FILE_PATH}{TABLE_NAME}.csv' {alias}".strip()
    print("TAB:: " + table_file_mapping[TABLE_NAME])

print("*"*100)

# for TABLE_NAME, INPUT_FILE_PATH in table_file_mapping.items():
#     FILTER_QUERY = re.sub(rf"\b{TABLE_NAME}\b", INPUT_FILE_PATH, FILTER_QUERY)
#     print(FILTER_QUERY)