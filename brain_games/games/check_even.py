import prompt
import random


def show_description():
    task = 'Answer "yes" if number even otherwise answer "no".'
    return task


def ask_question():
    number = random.randint(0, 100)
    print('Question:', number)
    answer = prompt.string('Your answer: ')
    if is_even(number):
        result = 'yes'
    else:
        result = 'no'
    return result, answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
