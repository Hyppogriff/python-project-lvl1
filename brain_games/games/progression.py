import random


TASK = 'What number is missing in the progression?'
MIN_INDEX_NUMBER = 0
LENGTH_PROGRESSION = 10
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 10
MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 10


def generate_question_and_answer():
    number_first = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    number_step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)
    progression = generate_progression(number_first, number_step)
    hidden_index = random.randint(MIN_INDEX_NUMBER, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    progression = ' '.join(str(value) for value in progression)
    question = "{}".format(progression)
    return correct_answer, question


def generate_progression(number_first, number_step):
    number_last = number_first + (LENGTH_PROGRESSION - 1) * number_step
    progression = list(range(number_first, number_last + number_step,
                       number_step))
    return progression
