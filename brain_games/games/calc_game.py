from brain_games.scripts.brain_games import greeting
from brain_games.cli import (
    welcome_user, question, rules_games, check_answer
                            )
import random


def game():
    greeting()
    print(rules_games('calc'))

    name = welcome_user()
    count = 0
    signs = ['+', '-', '*']

    while count < 3:
        number_one = random.randint(1, 99)
        number_two = random.randint(1, 99)
        random_sign = random.choices(signs)
        if random_sign[0] == '+':
            answer = number_one + number_two
        elif random_sign[0] == '-':
            answer = number_one - number_two
        else:
            answer = number_one * number_two

        user_answer = int(question('{}{}{}' .format(
            number_one, random_sign[0], number_two)))

        count = check_answer(user_answer, answer, name, count)

    print("Congratulations, {}!".format(name))
