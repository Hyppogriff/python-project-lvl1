import random


def show_description():
    task = 'Find the greatest common divisor of given numbers.'
    return task


def ask_question():
    number_1 = random.randint(1, 50)
    number_2 = random.randint(1, 50)
    question = "Question: {} {}".format(number_1, number_2)
    result = find_divisor(number_1, number_2)
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
