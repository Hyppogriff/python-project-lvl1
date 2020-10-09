import random


TASK = 'Answer "yes" if number even otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def ask_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = "{}".format(number)
    if is_even(number):
        result = 'yes'
    else:
        result = 'no'
    return result, question


def is_even(number):
    return number % 2 == 0
