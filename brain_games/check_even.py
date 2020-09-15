import prompt
import random


def even(name):
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                i += 1
                if i == 3:
                    print('Congratulations,', name)
                    break
            else:
                print('\'', answer, '\'', ' is wrong answer ;(. Correct\
 answer was \'yes\'.', sep='')
                print('Let\'s try again,', name)
                break
        elif number % 2 != 0:
            if answer == 'no':
                print('Correct!')
                i += 1
                if i == 3:
                    print('Congratulations,', name)
                    break
            else:
                print('\'', answer, '\'', ' is wrong answer ;(. Correct\
 answer was \'no\'.', sep='')
                print('Let\'s try again,', name)
                break
