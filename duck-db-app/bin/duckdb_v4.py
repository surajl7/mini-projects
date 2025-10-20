
import duckdb
import pandas as pd

FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'
# FILE_NAME = 'sample_data.csv'

# DATA_TABLE = "'" + FILE_PATH + FILE_NAME + "'" 

"""
# 1 ----------------------------------
SELECT * FROM SAMPLE_DATA

# 2 ----------------------------------
SELECT * 
FROM SAMPLE_DATA
WHERE Name = 'Bob'

# 3 ----------------------------------
SELECT *
FROM SAMPLE_DATA
WHERE SALARY > 55000

# 4 ----------------------------------
SELECT SUM(SALARY)
FROM SAMPLE_DATA

# 5 ----------------------------------
SELECT SUM(SALARY)
FROM SAMPLE_DATA
WHERE NAME = 'Alice' AND NAME = 'EVA'
"""

# SQL_QUERY = input(f"Enter the query: \n") + "'" + FILE_PATH + input() + ".csv" + "'"

SQL_QUERY = input(f"Enter the query: \n")

# SQL_QUERY = 'SELECT * FROM TABLE_NAME'

KEYWORD_FROM = SQL_QUERY.upper().find(" FROM ") + len(" FROM ")
SELECT_ITEMS = SQL_QUERY[:KEYWORD_FROM]
TABLE_NAME = SQL_QUERY[KEYWORD_FROM:].split()[0]

# print(SELECT_ITEMS + TABLE_NAME)

SQL_QUERY_DB = SELECT_ITEMS + "'" + FILE_PATH + TABLE_NAME + ".csv" + "'"

print(duckdb.sql(SQL_QUERY_DB))
