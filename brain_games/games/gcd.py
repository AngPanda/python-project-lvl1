from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game_round():
    num_one = randint(1, 99)
    num_two = randint(1, 99)
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
