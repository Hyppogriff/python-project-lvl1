import prompt
import random


def show_description():
    task = 'What number is missing in the progression?'
    return task


def ask_question():
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
    number_last = number_first + 9 * number_step
    progression = []
    for value in range(number_first, number_last + number_step, number_step):
        progression.append(value)
    return progression


def print_question(progression):
    print('Question:', end=' ')
    for value in progression:
        print(value, end=' ')
    print('')
