
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


