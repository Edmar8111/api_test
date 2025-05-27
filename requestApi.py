from flask import Flask, jsonify, request
import requests
import flet as ft
import os


app = Flask(__name__)

data={"mensagem":"request message", "status":"API Online"}

@app.route('/api', methods=['GET'])
def get_data():
    if request.method=='GET':
        print('Request')
    with open('index.html', 'rb') as f:
        doc=f.read()
    return doc
@app.route('/page', methods=['GET'])
def requestPost():
    with open('index.html', 'rb') as f:
        doc=f.read()
    return doc
if __name__=='__main__':
    app.run(debug=True)


class requestApi:
    def __init__(self, value):
        with app.test_client() as client:
            response=client.post('/api', data={'data':1})
            print(response.data)
        return None
    def requestPost(self, endpoint):
        return 