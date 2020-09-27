import prompt
import random
import brain_games.cli


def progression(name):
    i = 0
    while i < 3:
        sequence = brain_games.cli.generate_progression()
        index = random.randint(0, 9)
        result = sequence.pop(index)
        sequence.insert(index, '..')
        print('Question:', end=' ')
        for value in sequence:
            print(value, end=' ')
        print('')
        answer = prompt.integer('Your answer: ')
        if brain_games.cli.isResult(result, answer, name):
            i += 1
        else:
            break
    brain_games.cli.check_counter(i, name)
