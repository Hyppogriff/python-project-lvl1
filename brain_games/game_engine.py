import prompt


NUMBER_ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'


def run_game(game):
    print(GREETING)
    print(game.TASK, '\n')
    name = "{}!".format(prompt.string('May I have your name? '))
    print('Hello, {}\n'.format(name))
    for counter in range(NUMBER_ROUNDS):
        correct_answer, question = game.generate_question_and_answer()
        print("Question: {}".format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print_wrong_message(correct_answer, user_answer, name)
            break
    else:
        print('Congratulations, {}'.format(name))


def print_wrong_message(res, ans, name):
    text = "'{}' is wrong answer ;(. Correct answer was '{}'".format(ans, res)
    print(text)
    print('Let\'s try again, {}'.format(name))
