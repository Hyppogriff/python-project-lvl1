import prompt


def welcome_user():
    name = prompt.string('May I have your name? ') + '!'
    print('Hello,', name, '\n')
    return name


def is_correct_answer(result, answer):
    if result == answer:
        return True
    else:
        return False


def greeting():
    print('Welcome to the Brain Games!')


def check_win_counter(counter, win_counter, name):
    if counter == win_counter:
        print('Congratulations,', name)
