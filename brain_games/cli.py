import prompt


def welcome_user():
    name = prompt.string('May I have your name? ') + '!'
    print('Hello,', name, '\n')
    return name


def is_correct_answer(result, answer):
    if str(result) == answer:
        return True
    else:
        return False


def greeting():
    text = 'Welcome to the Brain Games!'
    print(text)


def check_win_counter(counter, win_counter, name):
    if counter == win_counter:
        print('Congratulations,', name)


def print_correct_message():
    print('Correct!')


def print_wrong_message(res, ans, name):
    text = "'{}' is wrong answer ;(. Correct answer was '{}'".format(ans, res)
    print(text)
    print('Let\'s try again,', name)
