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
    return question, correct_answer


def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for value in range(3, int(number**0.5) + 1, 2):
        if number % value == 0:
            return False
    return True
