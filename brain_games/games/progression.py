from random import randint


DESCRIPTION = "What number is missing \033[1min\033[0m the progression?"


def game_round():
    step = randint(1, 10)
    start_point = randint(1, 99)
    end_point = start_point + step * 10
    sequnce = list(range(start_point, end_point, step))
    gap_index = randint(0, 9)
    answer = str(sequnce[gap_index])
    sequnce[gap_index] = '..'
    question = ''
    for element in sequnce:
        question += str(element) + ' '
    return(question, answer)
