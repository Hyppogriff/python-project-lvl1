import prompt
import random


def calc(name):
    i = 0
    while i < 3:
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 10)
        sequence = ['+', '-', '*']
        operation = random.choice(sequence)
        print('Question:', number1, operation, number2)
        answer = prompt.integer('Your answer: ')
        if operation == '+':
            result = number1 + number2
            if result == answer:
                print('Correct!')
                i += 1
            else:
                print(answer, 'is wrong answer ;(. Correct answer was', result)
                print('Let\'s try again,', name)
                break
        elif operation == '-':
            result = number1 - number2
            if result == answer:
                print('Correct!')
                i += 1
            else:
                print(answer, 'is wrong answer ;(. Correct answer was', result)
                print('Let\'s try again,', name)
                break
        elif operation == '*':
            result = number1 * number2
            if result == answer:
                print('Correct!')
                i += 1
            else:
                print(answer, 'is wrong answer ;(. Correct answer was', result)
                print('Let\'s try again,', name)
                break
    if i == 3:
        print('Congratulations,', name)
