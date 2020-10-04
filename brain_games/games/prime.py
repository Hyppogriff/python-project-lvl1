import random


def show_description():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


def ask_question():
    number = random.randint(1, 50)
    result = 'no'
    if is_prime(number):
        result = 'yes'
    question = "Question: {}".format(number)
    return result, question


def is_prime(number):
    for value in range(number - 1, 1, -1):
        if not number % value:
            return False
    return True
