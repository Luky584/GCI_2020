import flask
from flask import request, send_file

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])

def home():
    return "loves contributing to ScoreLab."

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
