# use Python 3.7.0 64-bit ('base':conda) environment
import pandas as pd, pandas.io.sql, pyodbc

# Parameters
driver = '{ODBC Driver 13 for SQL Server}'
server = 'STP-DR'
db = 'STP_Reporting'
uid = ''
pwd = ''

# connection String
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + 
    db + ';Trusted_Connection=yes;')

# Query
sql = '''

select top 10 *
from PAT_PatientID_Index

'''

# Create dataframe

df = pd.read_sql(sql,conn)

# Print data

print(df)

