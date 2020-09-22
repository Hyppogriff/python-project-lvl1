import prompt
import random


def prime(name):
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        result = 'yes'
        for value in range(number - 1, 1, -1):
            if not number % value:
                result = 'no'
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            i += 1
        else:
            print('\'', answer, '\' ', 'is wrong answer ;(. Correct\
 answer was ', '\'', result, '\'', sep='')
            print('Let\'s try again,', name)
            break
    if i == 3:
        print('Congratulations,', name)
