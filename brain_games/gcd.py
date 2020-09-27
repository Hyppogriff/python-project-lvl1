import prompt
import random
import brain_games.cli


def gcd(name):
    i = 0
    while i < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print('Question:', number1, number2)
        answer = prompt.integer('Your answer: ')
        number_divisor = min(number1, number2)
        while number_divisor > 0:
            if (max(number1, number2) % number_divisor == 0 and
                    min(number1, number2) % number_divisor == 0):
                result = number_divisor
                break
            number_divisor -= 1
        if brain_games.cli.isResult(result, answer, name):
            i += 1
        else:
            break
    brain_games.cli.check_counter(i, name)
