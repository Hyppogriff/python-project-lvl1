import prompt
import random
import brain_games.cli


def calc(name):
    i = 0
    while i < 3:
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 10)
        sequence = ['+', '-', '*']
        operation = random.choice(sequence)
        print('Question:', number1, operation, number2)
        answer = prompt.integer('Your answer: ')
        if operation == '+':
            result = number1 + number2
            if brain_games.cli.isResult(result, answer, name):
                i += 1
            else:
                break
        elif operation == '-':
            result = number1 - number2
            if brain_games.cli.isResult(result, answer, name):
                i += 1
            else:
                break
        elif operation == '*':
            result = number1 * number2
            if brain_games.cli.isResult(result, answer, name):
                i += 1
            else:
                break
    brain_games.cli.check_counter(i, name)
