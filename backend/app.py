from flask import Flask, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)
envr = os.environ.get("FLASK_ENV")

# envr = ''

@app.route('/')

def hello():
    return {'data':'hello'+' '+ envr}

# if __name__ == '__main__':
#     hello()
#     app.run('localhost', 7001)


    