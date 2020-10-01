import prompt
import random


def question():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    print('Question:', number1, number2)
    answer = prompt.integer('Your answer: ')
    result = find_divisor(number1, number2)
    return result, answer


def find_divisor(number1, number2):
    number_divisor = min(number1, number2)
    while number_divisor > 0:
        if (max(number1, number2) % number_divisor == 0 and
                min(number1, number2) % number_divisor == 0):
            result = number_divisor
            break
        number_divisor -= 1
    return result
