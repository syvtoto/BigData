
from flask import Flask
import pandas as pd
app = Flask(__name__)

data = pd.read_json('reduce.json')
print(data.head())

@app.route('/')
def hello_world():
    return 'Hello, World From a Docker container'

@app.route('/books')
def getBooks():
    return data.head().to_json(orient='records')

@app.route('/book/<isbn>')
def getBookByISBN(isbn):
    return data[data['isbn'] == isbn].to_dict()
