import random


TASK = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 50


def generate_question_and_answer():
    number_1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = "{} {}".format(number_1, number_2)
    correct_answer = str(find_divisor(number_1, number_2))
    return correct_answer, question


def find_divisor(number_1, number_2):
    number_divisor = min(number_1, number_2)
    while number_divisor > 0:
        if (max(number_1, number_2) % number_divisor == 0 and
                min(number_1, number_2) % number_divisor == 0):
            correct_answer = number_divisor
            break
        number_divisor -= 1
    return correct_answer
