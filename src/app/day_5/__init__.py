from flask import Flask
import pandas as pd
import re
import math

app = Flask(__name__)

def day_5_response(partA):
    app.logger.info('Day 5 Module')
    if partA == True:
        data = pd.read_csv("data/day_5/day5a.csv", header=None)
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            
        
        result = result + "<br/>"
        result = result + str(total) + "<br/>"
    elif partA == False: 
        data = pd.read_csv("data/day_5/day5b.csv", header=None)
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
        

        result = result + "<br/>"
        result = result + str(total) + "<br/>"
        
    return result
