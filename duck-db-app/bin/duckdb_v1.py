
import duckdb
import pandas as pd

# print(duckdb.read_csv("C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\\business_data.csv"))
print(duckdb.read_csv("C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\sample_data.csv"))

# print(duckdb.sql("SELECT * FROM SAMPLE_DATA.CSV"))
print(duckdb.sql("SELECT * FROM SAMPLE_DATA.CSV WHERE NAME = 'Bob'"))

# print(duckdb.sql("SELECT * FROM 'C:\MYDATA\TRAINING\MiniProjects\DuckDB\inbox\sample_data.csv'"))


sql_query = input("Enter your query: \n")

print(duckdb.sql(sql_query))

