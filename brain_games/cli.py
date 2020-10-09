import prompt


def get_user_name():
    name = prompt.string('May I have your name? ')
    name = "{}!".format(name)
    return name


def is_correct_answer(result, answer):
    return result == answer


def print_wrong_message(res, ans, name):
    text = "'{}' is wrong answer ;(. Correct answer was '{}'".format(ans, res)
    print(text)
    print('Let\'s try again,', name)
