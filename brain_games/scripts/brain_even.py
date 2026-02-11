import random

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if number % 2 == 0 and answer == 'yes':
            print("Correct!")
            
        elif number % 2 != 0 and answer == 'no':
            print("Correct!")
            
        else:
            if number % 2 == 0:
                rightanswer = 'yes'
            else:
                rightanswer = 'no'
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {rightanswer}."
                )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


