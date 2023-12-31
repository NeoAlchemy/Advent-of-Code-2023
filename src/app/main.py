from flask import Flask, render_template
from day_1 import day_1_response
from day_2 import day_2_response
from day_3 import day_3_response
from day_4 import day_4_response
from day_5 import day_5_response

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.info('A value for debugging')
    return render_template('main.html', name="Ryan")


@app.route('/day-1')
def day1():
   app.logger.debug('day 1')
   response = day_1_response(partA=False)
   return response

@app.route('/day-2')
def day2():
   app.logger.debug('day 2')
   response = day_2_response(partA=False)
   return response

@app.route('/day-3')
def day3():
   app.logger.debug('day 3')
   response = day_3_response(partA=False)
   return response

@app.route('/day-4')
def day4():
   app.logger.debug('day 4')
   response = day_4_response(partA=False)
   return response

@app.route('/day-5')
def day5():
   app.logger.debug('day 5')
   response = day_5_response(partA=True)
   return response

if __name__ == "__main__":
  app.run(debug=True)