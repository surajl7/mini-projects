
import duckdb
import pandas as pd

FILE_PATH = r'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\'
FILE_NAME = 'sample_data.csv'

DATA_TABLE = "'" + FILE_PATH + FILE_NAME + "'" 

# SQL_QUERY = f"SELECT * FROM {DATA_TABLE}"

# print(SQL_QUERY)

# print(duckdb.sql(SQL_QUERY))

# sql_query = input("Enter your query: \n")

# print(duckdb.sql(sql_query))

# SQL_QUERY = input(f"Enter the query: \n")

# TABLE_NAME = "'" + FILE_PATH + input() + ".csv" + "'"

# print(SQL_QUERY)
# print(TABLE_NAME)

SQL_QUERY = input(f"Enter the query: \n") + "'" + FILE_PATH + input() + ".csv" + "'"

print(SQL_QUERY)

print(duckdb.sql(SQL_QUERY))



