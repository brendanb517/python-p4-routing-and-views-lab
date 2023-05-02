#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:param>")
def print_string(param):
    print(param)
    return f"{param}"

@app.route("/count/<int:number>")
def count(number):
    numbers = ""
    for num in range(number):
        numbers = numbers + f"{num}\n"
    return numbers

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    if operation == "+":
        return f"{int(num1) + int(num2)}"
    elif operation == "-":
        return f"{int(num1) - int(num2)}"
    elif operation == "*":
        return f"{int(num1) * int(num2)}"
    elif operation == "div":
        return f"{int(num1) / int(num2)}"
    elif operation == "%":
        return f"{int(num1) % int(num2)}"
    else:
        return "Invalid operation"
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
