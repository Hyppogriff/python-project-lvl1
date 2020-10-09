import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 50


def ask_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    result = 'no'
    if is_prime(number):
        result = 'yes'
    question = "{}".format(number)
    return result, question


def is_prime(number):
    if number <= 1:
        raise ValueError("Wrong number")
    for value in range(number - 1, MIN_NUMBER, -1):
        if not number % value:
            return False
    return True
