from flask import render_template
from app import app
from modules.calculator import add, subtract, multiply, divide

@app.route('/add/<num1>/<num2>')
def add_num(num1, num2):
    answer = add(int(num1), int(num2))
    output = str(num1) + " + " + str(num2) + " = " + str(answer)
    return render_template('index.html', output=output)

@app.route('/subtract/<num1>/<num2>')
def subtract_num(num1, num2):
    answer = subtract(int(num1), int(num2))
    output = str(num1) + " - " + str(num2) + " = " + str(answer)
    return render_template('index.html', output=output)

@app.route('/multiply/<num1>/<num2>')
def multiply_num(num1, num2):
    answer = multiply(int(num1), int(num2))
    output = str(num1) + " * " + str(num2) + " = " + str(answer)
    return render_template('index.html', output=output)

@app.route('/divide/<num1>/<num2>')
def divide_num(num1, num2):
    answer = divide(int(num1), int(num2))
    output = str(num1) + " / " + str(num2) + " = " + str(answer)
    return render_template('index.html', output=output)


