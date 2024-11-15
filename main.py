from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/A1G/<int:x>")
def division(x):
    return str(x*x)

@app.route("/A1F/<int:price>,<int:discount>")
def apply_discount(price, discount):
    new_price = price - (price * discount/100)
    return str(round(new_price, 2))

@app.route("/A1E/Prozedural")
def calculate_sum(numbers):
    return sum(numbers)
def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers) if numbers else 0

@app.route("/A1E/Funktional")
def functional(numbers):
    calc_sum = lambda numbers: sum(numbers)
    calc_average = lambda numbers: calculate_sum(numbers) / len(numbers) if numbers else 0
    return calc_sum,calc_average

@app.route("/B1G/<int:number>")
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return f"Die Zahl {number} ist keine Primzahl"
    return f"Die Zahl {number} ist eine Primzahl"

# Ab hier Code für B1F
def validate_input(number):
    return isinstance(number, int) and number > 1

def is_divisible(number, divisor):
    return number % divisor == 0

def is_prime_num(number):
    if not validate_input(number):
        return "Die Eingabe muss eine ganze Zahl größer als 1 sein."

    for i in range(2, int(number ** 0.5) + 1):
        if is_divisible(number, i):
            return f"Die Zahl {number} ist keine Primzahl."
    return f"Die Zahl {number} ist eine Primzahl."


@app.route("/B1F/<int:number>")
def check_prime(number):
    result = is_prime_num(number)
    return result

#Ab hier Code für B1E
def fibonacci(n):
    if n < 0:
        raise ValueError("Die Position muss eine nicht-negative Zahl sein.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence(length):
    if length <= 0:
        return []
    return [fibonacci(i) for i in range(length)]

@app.route("/B1E/<int:number>")
def get_fibonacci_sequence(number):
    try:
        sequence = fibonacci_sequence(number)
        return jsonify(sequence)
    except ValueError as e:
        return str(e), 400


@app.route("/B2G")
def greeting():
    name = request.args.get("name", "Guest")
    return f"Hallo, {name}!"

def output(function,name):
    print(function(name))


#ab hier Code B2F
def use_operation(funktion, zahl):
    return funktion(zahl)


def double(x):
    return x * 2

@app.route('/B2F', methods=['GET'])
def verdoppeln_route():
    number = int(request.args.get('zahl', 1))
    result = use_operation(double, number)
    return jsonify({"ergebnis": result})

#ab hier Code B2E
def outer_function(x):
    def inner_function(y):
        return x*y
    return inner_function

closure = outer_function(10)

@app.route("/B2E/<int:y>")
def get_value(y):
    result = closure(y)
    return jsonify({"Resultat":result})

@app.route('/B3G', methods=['GET'])
def convert_to_uppercase():
    text = request.args.get("text", "")
    convert_lambda = lambda x: x.upper()
    result = convert_lambda(text)
    return jsonify({"original_text": text, "uppercase_text": result})


@app.route('/B3F', methods=['GET'])
def add_and_multiply():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    add_and_multiply_lambda = lambda x, y: (x + y) * y
    result = add_and_multiply_lambda(num1, num2)

    return jsonify({"result": result})


@app.route('/B3E', methods=['GET'])
def sort_people():
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "Diana", "age": 28}
    ]

    reverse = request.args.get("reverse", "false").lower() == "true"
    people_sorted = sorted(people, key=lambda x: x["age"], reverse=reverse)
    return jsonify({"sorted_people": people_sorted})

if __name__ == '__main__':
    app.run(debug=True)