import prompt
import random


def question():
    progression = generate_progression()
    index = random.randint(0, 9)
    result = progression.pop(index)
    progression.insert(index, '..')
    print_question(progression)
    answer = prompt.integer('Your answer: ')
    return result, answer


def generate_progression():
    number_first = random.randint(1, 10)
    number_step = random.randint(1, 10)
    number_last = number_first
    number = 1
    progression = []
    while number < 10:
        number_last = number_last + number_step
        number += 1
    for value in range(number_first, number_last + number_step, number_step):
        progression.append(value)
    return progression


def print_question(progression):
    print('Question:', end=' ')
    for value in progression:
        print(value, end=' ')
    print('')
