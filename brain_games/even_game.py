from brain_games.scripts.brain_games import greeting, rules_games
from brain_games.cli import welcome_user, question
import random
import sys


def game():
    greeting()
    print(rules_games('even'))
    name = welcome_user()
    count_answers = 0
    while count_answers < 3:
        number = random.randint(1, 99)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        user_answer = question(number)
        if user_answer == correct_answer:
            count_answers += 1
            print("Correct!")
        else:
            sys.exit(
                  "'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!"
                  .format(user_answer, correct_answer, name)
                  )

    print("Congratulations, {}!" .format(name))
