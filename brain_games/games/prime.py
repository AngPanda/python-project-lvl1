from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_round():
    question = randint(1, 99)
    answer = is_prime(question)
    return(question, answer)


def is_prime(number):
    if number == 2:
        return 'yes'
    devider = 3
    while devider <= number / 2:
        if number % devider == 0:
            return 'no'
        else:
            devider += 1
    return 'yes'
