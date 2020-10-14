import prompt


def get_user_name():
    name = prompt.string('May I have your name? ')
    name = "{}!".format(name)
    return name
