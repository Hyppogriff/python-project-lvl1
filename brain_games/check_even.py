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
            if brain_games.cli.isResult('yes', answer, name):
                i += 1
            else:
                break
        elif number % 2 != 0:
            if brain_games.cli.isResult('no', answer, name):
                i += 1
            else:
                break
    brain_games.cli.check_counter(i, name)
