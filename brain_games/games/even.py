from random import randrange


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUMBERS = 100


def game_round():
    number = randrange(MAX_NUMBERS)
    answer = 'yes' if number % 2 == 0 else 'no'
    return (number, answer)
