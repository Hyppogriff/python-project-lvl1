import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDOM_NUMBER = 2
MAX_RANDOM_NUMBER = 50


def generate_question_and_answer():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = 'no'
    if is_prime(number):
        correct_answer = 'yes'
    question = str(number)
    return correct_answer, question


def is_prime(number):
    if number <= 1:
        raise ValueError("Wrong number")
    for value in range(number - 1, MIN_RANDOM_NUMBER, -1):
        if not number % value:
            return False
    return True
