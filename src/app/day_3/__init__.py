from flask import Flask
import pandas as pd
import re

app = Flask(__name__)

def day_2_response(partA):
    app.logger.info('Day 3 Module')
    if partA == True:
        data = pd.read_csv("data/day_3/day3a.csv", header=None, sep="|")
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            
    elif partA == False: 
        data = pd.read_csv("data/day_2/day2b.csv", header=None, sep="|")
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
        
    return result