from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def game_round():
    number = randint(1, 99)
    answer = 'yes' if number % 2 == 0 else 'no'
    return(number, answer)
