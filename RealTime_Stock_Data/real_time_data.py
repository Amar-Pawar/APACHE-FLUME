'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-08-04
@Last Modified by: Amar Pawar
@Last Modified time: 2021-08-04
@Title : Program to store tral time data on HDFS with flume
/**********************************************************************************
'''
import csv
import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

my_data = os.getenv("KEY")
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey={}'.format(my_data)

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)