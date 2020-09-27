import prompt
import random
import brain_games.cli


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
        if brain_games.cli.isResult(result, answer, name):
            i += 1
        else:
            break
    brain_games.cli.check_counter(i, name)
