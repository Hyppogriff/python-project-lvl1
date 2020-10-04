import random


def show_description():
    task = 'What is the result of the expression?'
    return task


def ask_question():
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = "Question: {} {} {}".format(number_1, operation, number_2)
    result = check_operation(operation, number_1, number_2)
    return result, question


def check_operation(operation, number_1, number_2):
    if operation == '+':
        result = number_1 + number_2
    elif operation == '-':
        result = number_1 - number_2
    elif operation == '*':
        result = number_1 * number_2
    else:
        print('Unknown operation:', operation)
    return result
