import os
import sys
from src.End_to_End_ML_Project.exception import CustomException
from src.End_to_End_ML_Project.logger import logging
from dotenv import load_dotenv
import pandas as pd
import pymysql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
passw = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info("reading SQL Database started")
    try:
        mydb = pymysql.connect(host = host,
                               user = user,
                               password = passw,
                               db = db)
        logging.info("Connection Established", mydb)
        df = pd.read_sql_query("Select * from students", mydb)
        print(df.head())

        return df
    
    except Exception as e:
        raise CustomException(e, sys)
