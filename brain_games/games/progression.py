from random import randrange, randint


DESCRIPTION = "What number is missing in the progression?"
SEQUNCE_LENGTH = 10
MAX_START_POINT = 100


def game_round():
    step = randint(1, 10)
    start_point = randrange(MAX_START_POINT)
    end_point = start_point + step * SEQUNCE_LENGTH
    sequnce = list(range(start_point, end_point, step))
    gap_index = randrange(SEQUNCE_LENGTH)
    answer = str(sequnce[gap_index])
    sequnce[gap_index] = '..'
    question = ''
    for element in sequnce:
        question += str(element) + ' '
    return(question, answer)
