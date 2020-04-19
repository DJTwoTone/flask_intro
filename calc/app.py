from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def adding():
    a = request.args['a']
    b = request.args['b']
    return f"""{add(int(a), int(b))}"""

@app.route("/sub")
def subbing():
    a = request.args['a']
    b = request.args['b']
    return f"""{sub(int(a), int(b))}"""

@app.route("/mult")
def multing():
    a = request.args['a']
    b = request.args['b']
    return f"""{mult(int(a), int(b))}"""

@app.route("/div")
def divving():
    a = request.args['a']
    b = request.args['b']
    return f"""{div(int(a), int(b))}"""

ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operation>")
def all(operation):
    a = request.args['a']
    b = request.args['b']
    return f"""{ops[operation](int(a), int(b))}"""