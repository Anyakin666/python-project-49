import random

RULES = 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(['+', '-', '*'])
    
    if op == '+':
        correct = num1 + num2
    elif op == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2
    
    question = f"{num1} {op} {num2}"
    return question, str(correct)