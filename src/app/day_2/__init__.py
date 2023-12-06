from flask import Flask
import pandas as pd
import re

app = Flask(__name__)

def day_2_response(partA):
    app.logger.info('Day 2 Module')
    if partA == True:
        data = pd.read_csv("data/day_2/day2a.csv", header=None, sep="|")
        result = ""
        total = 0
        for index, row in data.iterrows():
            app.logger.debug(row[0])
            result = result + row[0] 
            matches = re.findall(r"^Game\s(\d+):", row[0])
            for match in matches:
                app.logger.debug(match)
                result = result + " >> " + str(match)
            
            blue = 0
            red = 0
            green = 0
            gameset = re.findall(r"(?=:|;)(.+)(?=;|\Z)", row[0])
            for aset in gameset:
                app.logger.debug(aset)
                blues = re.findall(r"(\d+)\sblue", aset)
                for blueCount in blues:
                    blue = max(int(blue), int(blueCount))
                result = result + "  " + str(blue) + " &#128998;"

                reds = re.findall(r"(\d+)\sred", aset)
                for redCount in reds:
                    red = max(int(red), int(redCount))
                result = result + "  " + str(red) + " &#128997;"

                greens = re.findall(r"(\d+)\sgreen", aset)
                for greenCount in greens:
                    green = max(int(green), int(greenCount))
                result = result + "  " + str(green) + " &#129001;"

            if (blue <= 14) & (red <= 12) & (green <= 13):
                total = total + int(match)
                result = result + " True";
            else:
                result = result + " False";
            result = result + "<br/>"
        result = result + str(total) + "<br/>"
    elif partA == False: 
        data = pd.read_csv("data/day_2/day2b.csv", header=None)
        result = ""
        total = 0
    return result