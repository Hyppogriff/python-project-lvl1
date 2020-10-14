import random


TASK = 'What is the result of the expression?'
MIN_RANDOM_NUMBER = 0
MAX_RANDOM_NUMBER = 10


def generate_question_and_answer():
    number_1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = "{} {} {}".format(number_1, operation, number_2)
    correct_answer = str(calculate_operation_result(operation, number_1,
                                                    number_2))
    return correct_answer, question


def calculate_operation_result(operation, number_1, number_2):
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    elif operation == '*':
        correct_answer = number_1 * number_2
    else:
        raise ValueError("Unknown operation")
    return correct_answer
