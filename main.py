from flask import Flask, json, request

app = Flask(__name__)



@app.route('/')
def receive():
    print(request.args)

    return 200