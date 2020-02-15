from random import randrange, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'
LIST_SIGNS = (('+', add), ('-', sub), ('*', mul))
MAX_NUMBER = 100


def game_round():
    number_one = randrange(MAX_NUMBER)
    number_two = randrange(MAX_NUMBER)
    sign, instruction = choice(LIST_SIGNS)
    answer = str(instruction(number_one, number_two))
    question = f'{number_one} {sign} {number_two}'
    return (question, answer)
