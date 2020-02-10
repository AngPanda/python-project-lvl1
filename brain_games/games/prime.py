from random import randrange


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def game_round():
    question = randrange(MAX_NUMBER)
    answer = 'yes' if is_prime(question) else 'no'
    return (question, answer)


def is_prime(number):
    if number == 2:
        return True
    devider = 3
    while devider <= number / 2:
        if number % devider == 0:
            return False
        else:
            devider += 1
    return True
