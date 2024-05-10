from flask import Flask, jsonify
from math import pi, log, log10
from num2words import num2words
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(n):
    return n == math.isqrt(n) ** 2

def is_odd(n):
    return n % 2 != 0

def square_root(n):
    return math.sqrt(n)

def is_perfect_cube(n):
    return n == round(n ** (1. / 3)) ** 3

def is_even(n):
    return n % 2 == 0

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def is_composite(n):
    return not is_prime(n) and n != 1

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def number_of_digits(n):
    return len(str(n))

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def reverse_number(n):
    return int(str(n)[::-1])

def numtimespi(n):
    return n * pi

def numtimeslog(n):
    return n * log(n)
def numtimeslog10(n):
    return n * log10(n)

@app.route('/convert/<int:receivedNum>', methods=['GET'])
def displaynum(receivedNum):
    words = num2words(receivedNum)
    return jsonify({
        'numberInWords': words,
        'isPrime': is_prime(receivedNum),
        'isPerfectSquare': is_perfect_square(receivedNum),
        'isOdd': is_odd(receivedNum),
        'squareRoot': square_root(receivedNum),
        'isPerfectCube': is_perfect_cube(receivedNum),
        'isEven': is_even(receivedNum),
        'decimalToBinary': decimal_to_binary(receivedNum),
        'isComposite': is_composite(receivedNum),
        'square': square(receivedNum),
        'cube': cube(receivedNum),
        'primeFactors': prime_factors(receivedNum),
        'numberOfDigits': number_of_digits(receivedNum),
        'sumOfDigits': sum_of_digits(receivedNum),
        'reverseNumber': reverse_number(receivedNum),
        'numtimespi': numtimespi(receivedNum),
        'numtimeslog': numtimeslog(receivedNum),
        'numtimeslog10': numtimeslog10(receivedNum)

        # Add more properties here
    })

if __name__ == '__main__':
    app.run(debug=True)