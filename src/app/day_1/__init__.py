from flask import Flask

app = Flask(__name__)

def day_1_response():
    app.logger.info('Day 1 Module')
    return "day 1!!"
