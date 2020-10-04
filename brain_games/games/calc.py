import prompt
import random


def show_description():
    task = 'What is the result of the expression?'
    return task


def ask_question():
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    print('Question:', number1, operation, number2)
    answer = prompt.integer('Your answer: ')
    result = check_operation(operation, number1, number2)
    return result, answer


def check_operation(operation, number1, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    else:
        print('Unknown operation:', operation)
    return result
