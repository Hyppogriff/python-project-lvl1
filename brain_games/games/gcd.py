import random


TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 50


def ask_question():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = "{} {}".format(number_1, number_2)
    result = str(find_divisor(number_1, number_2))
    return result, question


def find_divisor(number_1, number_2):
    number_divisor = min(number_1, number_2)
    while number_divisor > 0:
        if (max(number_1, number_2) % number_divisor == 0 and
                min(number_1, number_2) % number_divisor == 0):
            result = number_divisor
            break
        number_divisor -= 1
    return result
