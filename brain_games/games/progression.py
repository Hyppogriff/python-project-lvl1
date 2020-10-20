import random


TASK = 'What number is missing in the progression?'
MIN_INDEX_NUMBER = 0
LENGTH_PROGRESSION = 10
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 10
MIN_STEP_NUMBER = 1
MAX_STEP_NUMBER = 10


def generate_question_and_answer():
    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)
    progression = generate_progression(first_number, step)
    hidden_index = random.randint(MIN_INDEX_NUMBER, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(value) for value in progression)
    return question, correct_answer


def generate_progression(first_number, step):
    last_number = first_number + LENGTH_PROGRESSION * step
    progression = list(range(first_number, last_number,
                       step))
    return progression
