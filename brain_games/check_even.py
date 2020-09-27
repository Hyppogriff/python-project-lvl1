import prompt
import random
import brain_games.cli


def even(name):
    counter = brain_games.cli.counter()
    while counter > 0:
        number = random.randint(0, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        result = find_result(number)
        if brain_games.cli.isResult(result, answer, name):
            counter -= 1
        else:
            break
    brain_games.cli.check_counter(counter, name)


def find_result(number):
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result
