import random
import operator
import prompt

from brain_games.cli import welcome_user
def main():
    name = welcome_user()
    print("What is the result of the expression?")
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    for i in range(3):
        op_symbol = random.choice(list(operations.keys()))
        op_func = operations[op_symbol]
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        number = op_func(number1, number2)
        print(f"Question: {number1} {op_symbol} {number2}")
        answer = prompt.string("Your answer: ")
        if int(answer) == number:
            print("Correct!")
        else:
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {number}."
                )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")