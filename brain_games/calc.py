import prompt
import random
import brain_games.cli


def calc(name):
    counter = brain_games.cli.counter()
    while counter > 0:
        number1 = random.randint(0, 10)
        number2 = random.randint(0, 10)
        sequence = ['+', '-', '*']
        operation = random.choice(sequence)
        print('Question:', number1, operation, number2)
        answer = prompt.integer('Your answer: ')
        result = check_operation(operation, number1, number2)
        if brain_games.cli.isResult(result, answer, name):
            counter -= 1
        else:
            break
    brain_games.cli.check_counter(counter, name)


def check_operation(operation, number1, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    return result
