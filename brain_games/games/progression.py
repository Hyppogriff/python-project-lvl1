import random


TASK = 'What number is missing in the progression?'
MIN_INDEX_NUMBER = 0
MAX_INDEX_NUMBER = 9
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 10
MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 10


def ask_question():
    progression = generate_progression()
    index = random.randint(MIN_INDEX_NUMBER, MAX_INDEX_NUMBER)
    result = str(progression.pop(index))
    progression.insert(index, '..')
    string = get_string_from_progression(progression)
    question = "{}".format(string)
    return result, question


def generate_progression():
    number_first = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    number_step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)
    number_last = number_first + MAX_INDEX_NUMBER * number_step
    progression = []
    for value in range(number_first, number_last + number_step, number_step):
        progression.append(value)
    return progression


def get_string_from_progression(progression):
    string = ' '.join(str(value) for value in progression)
    return string
