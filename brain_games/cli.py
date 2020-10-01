import prompt


def welcome_user():
    name = prompt.string('May I have your name? ') + '!'
    print('Hello,', name, '\n')
    return name


def isResult(result, answer, name):
    if result == answer:
        print('Correct!')
        return True
    else:
        print('\'', answer, '\'', ' is wrong answer ;(. Correct answer \
 was ', '\'', result, '\'', sep='')
        print('Let\'s try again,', name)
        return False
