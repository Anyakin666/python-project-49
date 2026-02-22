import prompt

from brain_games.cli import welcome_user


def run(game_module):
    name = welcome_user()
    print(game_module.RULES)

    for _ in range(3):
        question, correct_answer = game_module.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")