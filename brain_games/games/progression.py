import random


def show_description():
    task = 'What number is missing in the progression?'
    return task


def ask_question():
    progression = generate_progression()
    index = random.randint(0, 9)
    result = progression.pop(index)
    progression.insert(index, '..')
    string = get_string_from_progression(progression)
    question = "Question: {}".format(string)
    return result, question


def generate_progression():
    number_first = random.randint(1, 10)
    number_step = random.randint(1, 10)
    number_last = number_first + 9 * number_step
    progression = []
    for value in range(number_first, number_last + number_step, number_step):
        progression.append(value)
    return progression


def get_string_from_progression(progression):
    string = ''
    for value in progression:
        string = string + str(value) + " "
    string = string.rstrip()
    return string
