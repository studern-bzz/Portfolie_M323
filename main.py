from flask import Flask, jsonify

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


if __name__ == '__main__':
    app.run(debug=True)