import prompt
import random


def show_description():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


def ask_question():
    number = random.randint(1, 50)
    result = check_number(number)
    print('Question:', number)
    answer = prompt.string('Your answer: ')
    return result, answer


def check_number(number):
    result = 'yes'
    for value in range(number - 1, 1, -1):
        if not number % value:
            result = 'no'
    return result
