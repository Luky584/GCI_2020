import flask
from flask import request, send_file

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])

def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000)