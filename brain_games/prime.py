import prompt
import random
import brain_games.cli


def prime(name):
    counter = brain_games.cli.counter()
    while counter > 0:
        number = random.randint(1, 50)
        result = 'yes'
        for value in range(number - 1, 1, -1):
            if not number % value:
                result = 'no'
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if brain_games.cli.isResult(result, answer, name):
            counter -= 1
        else:
            break
    brain_games.cli.check_counter(counter, name)
