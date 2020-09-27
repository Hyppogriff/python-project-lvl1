import prompt
import random
import brain_games.cli


def progression(name):
    counter = brain_games.cli.counter()
    while counter > 0:
        sequence = generate_progression()
        index = random.randint(0, 9)
        result = sequence.pop(index)
        sequence.insert(index, '..')
        print_question(sequence)
        answer = prompt.integer('Your answer: ')
        if brain_games.cli.isResult(result, answer, name):
            counter -= 1
        else:
            break
    brain_games.cli.check_counter(counter, name)


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


def print_question(sequence):
    print('Question:', end=' ')
    for value in sequence:
        print(value, end=' ')
    print('')
