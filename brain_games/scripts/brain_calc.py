#!/usr/bin/env python
import random
import prompt
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print('What is the result of the expression?')
    
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        op = random.choice(['+', '-', '*'])
        
        if op == '+':
            correct = num1 + num2
        elif op == '-':
            correct = num1 - num2
        else:
            correct = num1 * num2
            
        print(f'Question: {num1} {op} {num2}')
        answer = prompt.string('Your answer: ')
        
        if int(answer) == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()