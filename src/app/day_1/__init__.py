from flask import Flask
import pandas as pd
import re

app = Flask(__name__)

def day_1_response(partA):
    app.logger.info('Day 1 Module')
    if partA == True:
        data = pd.read_csv("data/day_1/day1a.csv", header=None)
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            matchedResults = re.findall(r"\d", str(row[0]))
            digit1 = matchedResults[0]
            digit2 = matchedResults[-1]
            result = result + str(digit1) + "" + str(digit2) + "<br>"
            total = total + int(str(digit1) + "" + str(digit2))
            app.logger.debug(str(digit1) + "" + str(digit2))
        result = result + "<br>" + str(total)
    elif partA == False: 
        data = pd.read_csv("data/day_1/day1b.csv", header=None)
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            originalstring = row[0]
            row[0] = row[0].replace("oneight", "oneeight")
            row[0] = row[0].replace("twone", "twoone")
            row[0] = row[0].replace("threeight", "threeeight")
            row[0] = row[0].replace("fiveight", "fiveeight")
            row[0] = row[0].replace("sevenine", "sevenine")
            row[0] = row[0].replace("eightwo", "eighttwo")
            row[0] = row[0].replace("eightthree", "eightthree")
            row[0] = row[0].replace("nineight", "nineeight")
            pattern = re.compile(r"(\d|two|eight|five|one|three|four|six|nine|seven)");
            matchedResults = [ match.group for match in pattern.finditer(row[0]) ]
            mapping = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
            digit1 = matchedResults.pop(0)(0)
            
            if (len(matchedResults) == 0):
                digit2 = digit1
            else:
                dig2 = matchedResults.pop()
                digit2 = dig2(0)
            
            if digit1.isnumeric():
                digit1 = digit1
            else:
                digit1 = mapping[digit1]
            if digit2.isnumeric():
                digit2 = digit2
            else:
                digit2 = mapping[digit2]
                
            
            result = result + originalstring + " >> " + str(digit1) + "" + str(digit2) + "<br>"
            total = total + int(str(digit1) + "" + str(digit2))
            app.logger.debug(str(digit1) + "" + str(digit2))
        result = result + "<br>" + str(total)
    return result;

