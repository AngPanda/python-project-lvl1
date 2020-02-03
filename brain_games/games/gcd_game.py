from brain_games.scripts.brain_games import greeting
from brain_games.cli import (
    welcome_user, question, rules_games, check_answer, gcd
                            )
import random


def game():
    greeting()
    print(rules_games('gcd'))
    count = 0
    name = welcome_user()

    while count < 3:
        num_one = random.randint(1, 99)
        num_two = random.randint(1, 99)
        answer = gcd(num_one, num_two)
        user_answer = int(question('{} {}' .format(num_one, num_two)))
        count = check_answer(user_answer, answer, name, count)

    print("Congratulations, {}!" .format(name))
