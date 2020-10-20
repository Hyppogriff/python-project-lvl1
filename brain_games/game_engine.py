import prompt


NUMBER_OF_ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'


def run_game(game):
    print(GREETING)
    print(game.TASK, '\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.generate_question_and_answer()
        print("Question: {}".format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. \
 Correct answer was '{}'".format(user_answer, correct_answer))
            print('Let\'s try again, {}!'.format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
