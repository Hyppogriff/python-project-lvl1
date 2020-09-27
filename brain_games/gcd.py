import prompt
import random
import brain_games.cli


def gcd(name):
    counter = brain_games.cli.counter()
    while counter > 0:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)
        print('Question:', number1, number2)
        answer = prompt.integer('Your answer: ')
        result = find_divisor(number1, number2)
        if brain_games.cli.isResult(result, answer, name):
            counter -= 1
        else:
            break
    brain_games.cli.check_counter(counter, name)


def find_divisor(number1, number2):
    number_divisor = min(number1, number2)
    while number_divisor > 0:
        if (max(number1, number2) % number_divisor == 0 and
                min(number1, number2) % number_divisor == 0):
            result = number_divisor
            break
        number_divisor -= 1
    return result
