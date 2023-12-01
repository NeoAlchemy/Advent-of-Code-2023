from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.info('A value for debugging')
    return render_template('main.html', name="Ryan")



if __name__ == "__main__":
  app.run(debug=True)