import math
import random

RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct = math.gcd(number1, number2)
    return f"{number1} {number2}", str(correct)
