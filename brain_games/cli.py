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


def check_answer(user_answer, answer, count, name):
    if user_answer == answer:
        print("Correct!")
        return count + 1
    else:
        sys.exit("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                 "Let's try again, {}!"
                 .format(user_answer, answer, name))
