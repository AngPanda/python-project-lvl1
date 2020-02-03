import prompt
import sys


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'. format(name))
    return name


def question(number):
    print('Question: {}' .format(number))
    answer = prompt.string('Your answer: ')
    return answer


def rules_games(game_name):
    if game_name == 'even':
        return 'Answer "yes" if number even otherwise answer "no".\n'
    elif game_name == 'calc':
        return 'What is the result of the expression?\n'
    elif game_name == 'gcd':
        return 'Find the greatest common divisor of given numbers.\n'


def check_answer(user_answer, answer, name, count):
    if user_answer == answer:
        print("Correct!")
        return count + 1
    else:
        sys.exit("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                 "Let's try again, {}!"
                 .format(user_answer, answer, name))


def gcd(num_one, num_two):
    while num_one != 0 and num_two != 0:
        if num_one > num_two:
            num_one = num_one % num_two
        else:
            num_two = num_two % num_one
    return num_one + num_two
