from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def game_round():
    signs = {'+': add, '-': sub, '*': mul}
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    random_sign = choice(list(signs.keys()))
    answer = str(signs[random_sign](number_one, number_two))
    question = f'{number_one} {random_sign} {number_two}'
    return(question, answer)
