from brain_games.scripts.brain_games import greeting
from brain_games.cli import welcome_user, question, rules_games, check_answer
import random


def game():
    greeting()
    print(rules_games('even'))
    name = welcome_user()
    count = 0

    while count < 3:
        number = random.randint(1, 99)
        answer = 'yes' if number % 2 == 0 else 'no'
        user_answer = question(number)
        count = check_answer(user_answer, answer, count, name)

    print("Congratulations, {}!" .format(name))
