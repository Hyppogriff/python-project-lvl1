import brain_games.cli
import prompt


MIN_ROUND_NUMBER = 1
NUMBER_ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'


def run_game(game):
    print(GREETING)
    print(game.TASK, '\n')
    name = brain_games.cli.get_user_name()
    print('Hello, {}'.format(name), '\n')
    for counter in range(MIN_ROUND_NUMBER, NUMBER_ROUNDS + 1):
        correct_answer, question = game.generate_question_and_answer()
        print("Question: {}".format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print_wrong_message(correct_answer, user_answer, name)
            break
        if counter == NUMBER_ROUNDS:
            print('Congratulations, {}'.format(name))


def print_wrong_message(res, ans, name):
    text = "'{}' is wrong answer ;(. Correct answer was '{}'".format(ans, res)
    print(text)
    print('Let\'s try again, {}'.format(name))
