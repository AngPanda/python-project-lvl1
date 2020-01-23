import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'. format(name))
    return name


def question(number):
    print('Question: {}' .format(number))
    answer = prompt.string('Your answer: ')
    return answer
