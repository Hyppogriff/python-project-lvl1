import prompt
import random


def gcd(name):
    i = 0
    while i < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print('Question:', number1, number2)
        answer = prompt.integer('Your answer: ')
        number = min(number1, number2)
        while number > 0:
            if (max(number1, number2) % number == 0 and
                    min(number1, number2) % number == 0):
                result = number
                if result == answer:
                    print('Correct!')
                    i += 1
                    break
            number -= 1
        if result != answer:
            print(answer, 'is wrong answer ;( Correct answer was', result)
            print('Let\'s try again,', name)
            break
    if i == 3:
        print('Congratulations,', name)
