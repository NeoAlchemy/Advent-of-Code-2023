from flask import Flask
import pandas as pd
import re
import math

app = Flask(__name__)

def day_4_response(partA):
    app.logger.info('Day 4 Module')
    if partA == True:
        data = pd.read_csv("data/day_4/day4a.csv", header=None)
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            winningNumberRow = re.findall(r"Card\s+\d+:\s(.+)\|.*", row[0])
            winningNumberList = re.findall(r"(\d+)", str(winningNumberRow))
            app.logger.debug(winningNumberList)

            cardNumberRow = re.findall(r".*\|\s(.+)$", row[0])
            cardNumberList = re.findall(r"(\d+)", str(cardNumberRow))
            app.logger.debug(cardNumberList)

            matches = set(winningNumberList).intersection(cardNumberList)
            
            points = math.floor(math.pow(2, len(list(matches)) - 1))
            result = result + row[0] + " --> " + str(matches) + " ==> " + str(points) + "<br/>"
            total = total + int(points)
        
        result = result + "<br/>"
        result = result + str(total) + "<br/>"
    elif partA == False: 
        data = pd.read_csv("data/day_4/day4b.csv", header=None)
        result = ""
        total = 0
        grid = [1] * (len(data))
        app.logger.debug(grid)
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            winningNumberRow = re.findall(r"Card\s+\d+:\s(.+)\|.*", row[0])
            winningNumberList = re.findall(r"(\d+)", str(winningNumberRow))
            app.logger.debug(winningNumberList)

            cardNumberRow = re.findall(r".*\|\s(.+)$", row[0])
            cardNumberList = re.findall(r"(\d+)", str(cardNumberRow))
            app.logger.debug(cardNumberList)

            matches = set(winningNumberList).intersection(cardNumberList)
            
            _smallIndex = 0
            while _smallIndex < len(matches):
                _smallIndex = _smallIndex + 1
                grid[index + _smallIndex] = grid[index + _smallIndex] + (1 * grid[index])
            
            result = result + row[0] + " --> " + str(matches) + "<br/>"

            #for cards in grid:
            #    result = result + str(cards) + "<br>"
            
        for cards in grid:
            total = total + cards

        result = result + "<br/>"
        result = result + str(total) + "<br/>"
        
    return result
