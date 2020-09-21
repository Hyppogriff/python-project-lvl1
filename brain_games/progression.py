import prompt
import random


def progression(name):
    i = 0
    while i < 3:
        number_first = random.randint(1, 10)
        number_step = random.randint(1, 10)
        number_last = number_first
        number = 1
        sequence = []
        while number < 10:
            number_last = number_last + number_step
            number += 1
        index = random.randint(0, 9)
        for value in range(number_first, number_last + number_step,
                           number_step):
            sequence.append(value)
        result = sequence.pop(index)
        sequence.insert(index, '..')
        print('Question:', end=' ')
        for value in sequence:
            print(value, end=' ')
        print('')
        answer = prompt.integer('Your answer: ')
        if result == answer:
            print('Correct!')
            i += 1
        else:
            print(answer, 'is wrong answer ;(. Correct answer was', result)
            print('Let\'s try again,', name)
            break
    if i == 3:
        print('Congratulations,', name)
