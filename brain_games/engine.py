import prompt


ATTEMPTS = 3


def greeting(description=None):
    print("Welcome to the Brain Games!")
    if description is not None:
        print(description)
    name = prompt.string('\nMay I have your name? ')
    print(f'Hello, {name}!\n')
    return name


def run(game):
    name = greeting(game.DESCRIPTION)
    for i in range(ATTEMPTS):
        question, answer = game.game_round()
        user_answer = ask(question)
        if answer != user_answer:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}.\
                    \nLet's try again, {name}!")
            break
        else:
            print("Correct!")
    else:
        print(f'Congratulations, {name}!')


def ask(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer
