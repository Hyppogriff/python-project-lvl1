import random


TASK = 'Answer "yes" if number even otherwise answer "no".'
MIN_RANDOM_NUMBER = 0
MAX_RANDOM_NUMBER = 100


def generate_question_and_answer():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
