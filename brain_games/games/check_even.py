import prompt
import random


def question():
    number = random.randint(0, 100)
    print('Question:', number)
    answer = prompt.string('Your answer: ')
    result = find_result(number)
    return result, answer


def find_result(number):
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result
