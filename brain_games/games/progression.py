import random


TASK = 'What number is missing in the progression?'
MIN_INDEX_NUMBER = 0
MAX_INDEX_NUMBER = 9
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 10
MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 10


def generate_question_and_answer():
    number_first = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    number_step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)
    progression = generate_progression(number_first, number_step)
    index = random.randint(MIN_INDEX_NUMBER, MAX_INDEX_NUMBER)
    correct_answer = str(progression[index])
    progression[index] = '..'
    string = get_string_from_progression(progression)
    question = "{}".format(string)
    return correct_answer, question


def generate_progression(number_first, number_step):
    number_last = number_first + MAX_INDEX_NUMBER * number_step
    progression = list(range(number_first, number_last + number_step,
                       number_step))
    return progression


def get_string_from_progression(progression):
    string = ' '.join(str(value) for value in progression)
    return string
