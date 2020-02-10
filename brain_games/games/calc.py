from random import randrange, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'
LIST_SIGN = (('+', add), ('-', sub), ('*', mul))
MAX_NUMBER = 100


def game_round():
    number_one = randrange(MAX_NUMBER)
    number_two = randrange(MAX_NUMBER)
    random_sign = choice(LIST_SIGN)
    answer = str(random_sign[1](number_one, number_two))
    question = f'{number_one} {random_sign[0]} {number_two}'
    return (question, answer)
