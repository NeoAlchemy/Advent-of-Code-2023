from flask import Flask
import pandas as pd
import re

app = Flask(__name__)

def day_3_response(partA):
    app.logger.info('Day 3 Module')
    if partA == True:
        data = pd.read_csv("data/day_3/day3a.csv", header=None)
        result = ""
        total = 0
        grid = []
        foundParts = []
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            grid.append(list(row[0]))
            result = result + str(list(row[0]))  + "<br/>"
        adjacentToSymbol = False
        currentNumber = ""
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char.isdigit():
                    currentNumber = currentNumber + char;
                    reg =('[-@_!#$£%^&*(%)<>?/=|+}{~:0123456789]') #SYMBOL SEARCH WITH NUMBERS
                    reg2 = ('[-@_!#$£%^&*()<>?/=|+}{~:]')  #WITHOUT NUMBERS
                    if j > 0 : #anything left or right
                        if re.search(reg2, grid[i][j-1]):
                            adjacentToSymbol = True
                    if j < len(row) - 1:
                        if re.search(reg2, grid[i][j+1]):
                            adjacentToSymbol = True
                    if i > 0: #anything up or down
                        if re.search(reg, grid[i-1][j]):
                            adjacentToSymbol = True
                    if i < len(grid) - 1:
                        if re.search(reg, grid[i+1][j]):
                            adjacentToSymbol = True
                    if i > 0 and j > 0:
                        if re.search(reg, grid[i-1][j-1]):
                            adjacentToSymbol = True
                    if i > 0 and j < len(row) - 1:
                        if re.search(reg, grid[i-1][j+1]):
                            adjacentToSymbol = True
                    if i < len(grid) - 1 and j > 0:
                        if re.search(reg, grid[i+1][j-1]):
                            adjacentToSymbol = True
                    if i < len(grid) - 1 and j < len(row) - 1:
                        if re.search(reg, grid[i+1][j+1]):
                            adjacentToSymbol = True
                else:
                    if currentNumber != "":
                        result = result + currentNumber + " --> " + str(adjacentToSymbol) + "<br/>"
                        if adjacentToSymbol:
                            foundParts.append(currentNumber)
                    currentNumber = ""
                    adjacentToSymbol = False
        for number in list(foundParts):
            total = total + int(number)
        result = result + "<br/>"
        result = result + str(total) + "<br/>"
    elif partA == False: 
        data = pd.read_csv("data/day_3/day3b.csv", header=None)
        result = ""
        total = 0
        grid = []
        foundParts = []
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            grid.append(list(row[0]))
            result = result + str(list(row[0]))  + "<br/>"
        adjacentToSymbol = False
        currentNumber = ""
        group = []
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == "*":
                    reg =('[0123456789]') #SYMBOL SEARCH WITH NUMBERS
                    if j > 0 : #anything left
                        if re.search(reg, grid[i][j-1]):
                            group.append(findFullNumber(grid, i, j-1))
                    if j < len(row) - 1: #anything right
                        if re.search(reg, grid[i][j+1]):
                            group.append(findFullNumber(grid, i, j+1))
                    if i > 0: #anything up
                        if re.search(reg, grid[i-1][j]):
                            group.append(findFullNumber(grid, i-1, j))
                    if i < len(grid) - 1: #anything down
                        if re.search(reg, grid[i+1][j]):
                            group.append(findFullNumber(grid, i+1, j))
                    if i > 0 and j > 0: #anything Top Left
                        if re.search(reg, grid[i-1][j-1]):
                            group.append(findFullNumber(grid, i-1, j-1))
                    if i > 0 and j < len(row) - 1: # anything Top Right
                        if re.search(reg, grid[i-1][j+1]):
                            group.append(findFullNumber(grid, i-1, j+1))
                    if i < len(grid) - 1 and j > 0:  #anything Bottom Left
                        if re.search(reg, grid[i+1][j-1]):
                            group.append(findFullNumber(grid, i+1, j-1))
                    if i < len(grid) - 1 and j < len(row) - 1:  #anything bottom right
                        if re.search(reg, grid[i+1][j+1]):
                            group.append(findFullNumber(grid, i+1, j+1))
                    group = set(group)
                    result = result + str(group)
                    if len(group) > 1:
                        part = int(list(group)[0]) * int(list(group)[1])
                        foundParts.append(part)
                    group = []
        for number in list(foundParts):
            total = total + int(number)
        result = result + "<br/>"
        result = result + str(total) + "<br/>"
        
    return result


def findFullNumber(grid, col, row):
    currentNumber = ""
    if grid[col][row].isnumeric():
        index = row
        while index >= 0 and grid[col][index].isnumeric():
            index = index - 1
        index = index + 1
        while index <= len(grid[col]) - 1 and grid[col][index].isnumeric():
            currentNumber = currentNumber + grid[col][index]
            index = index + 1
    return currentNumber
    
