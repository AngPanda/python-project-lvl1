from random import randrange


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def game_round():
    num_one = randrange(MAX_NUMBER)
    num_two = randrange(MAX_NUMBER)
    answer = str(gcd(num_one, num_two))
    question = f"{num_one} {num_two}"
    return (question, answer)


def gcd(num_one, num_two):
    while num_one != 0 and num_two != 0:
        if num_one > num_two:
            num_one = num_one % num_two
        else:
            num_two = num_two % num_one
    return num_one + num_two
