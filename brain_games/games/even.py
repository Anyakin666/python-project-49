import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 100)
    correct = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct