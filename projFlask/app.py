from flask import Flask
import pandas as pd
import pickle
from model import ClassifModel
app = Flask(__name__)

classifModel = ClassifModel()
data = pd.read_json('books.json')
print(data.head())

@app.route('/')
def hello_world():
    return 'Hello, World From a Docker container with a class inside, fileName ='+classifModel.fileName

@app.route('/books')
def getBooks():
    return data.head().to_json(orient='records')

@app.route('/book/<isbn>')
def getBookByISBN(isbn):
    return data[data['isbn'] == isbn].to_dict()
