from flask import Flask, json, request

app = Flask(__name__)



@app.route('/')
def receive():
    bindata = request.data
    print(bindata)