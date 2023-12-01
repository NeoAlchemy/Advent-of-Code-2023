from flask import Flask, render_template
from day_1 import day_1_response

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.info('A value for debugging')
    return render_template('main.html', name="Ryan")


@app.route('/day-1')
def day1():
   app.logger.debug('day 1')
   response = day_1_response()
   return response


if __name__ == "__main__":
  app.run(debug=True)