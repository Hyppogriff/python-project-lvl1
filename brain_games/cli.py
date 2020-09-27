import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ') + '!'
    print('Hello,', name, '\n')
    return name


def generate_progression():
    number_first = random.randint(1, 10)
    number_step = random.randint(1, 10)
    number_last = number_first
    number = 1
    sequence = []
    while number < 10:
        number_last = number_last + number_step
        number += 1
    for value in range(number_first, number_last + number_step, number_step):
        sequence.append(value)
    return sequence


def isResult(result, answer, name):
    if result == answer:
        print('Correct!')
        return True
    else:
        print(answer, 'is wrong answer ;(. Correct answer was', result)
        print('Let\'s try again,', name)
        return False


def check_counter(i, name):
    if i == 3:
        print('Congratulations,', name)
