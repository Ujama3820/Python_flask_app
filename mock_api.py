from flask import Flask, jsonify, request, render_template
from calculator import Calculator

app = Flask(__name__)  # Make sure this is defined at the top before any routes
calc = Calculator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    try:
        if operation == 'add':
            result = calc.add(num1, num2)
        elif operation == 'subtract':
            result = calc.subtract(num1, num2)
        elif operation == 'multiply':
            result = calc.multiply(num1, num2)
        elif operation == 'divide':
            result = calc.divide(num1, num2)
        else:
            result = "Invalid operation"
    except ValueError as e:
        result = str(e)

    return f"<h2 class='result'>Result: {result}</h2><a href='/'>Back</a>"

@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = calc.add(a, b)
    return jsonify({'result': result})

@app.route('/api/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = calc.subtract(a, b)
    return jsonify({'result': result})

@app.route('/api/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = calc.multiply(a, b)
    return jsonify({'result': result})

@app.route('/api/divide', methods=['POST'])
def divide():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    try:
        result = calc.divide(a, b)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Cannot divide by zero'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
