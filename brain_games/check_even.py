import prompt
import random
import brain_games.cli


def even(name):
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        if brain_games.cli.isResult(result, answer, name):
            i += 1
        else:
            break
    brain_games.cli.check_counter(i, name)
