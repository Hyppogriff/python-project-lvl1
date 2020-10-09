import random


TASK = 'What is the result of the expression?'
MIN_NUMBER = 0
MAX_NUMBER = 10


def ask_question():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = "{} {} {}".format(number_1, operation, number_2)
    result = str(check_operation(operation, number_1, number_2))
    return result, question


def check_operation(operation, number_1, number_2):
    if operation == '+':
        result = number_1 + number_2
    elif operation == '-':
        result = number_1 - number_2
    elif operation == '*':
        result = number_1 * number_2
    else:
        raise ValueError("Unknown operation")
    return result
