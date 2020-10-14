import brain_games.cli
import prompt


MIN_ROUND_NUMBER = 1
WIN_COUNTER = 3
GREETING = 'Welcome to the Brain Games!'


def run_game(game):
    print(GREETING)
    print(game.TASK, '\n')
    name = brain_games.cli.get_user_name()
    print('Hello, {}'.format(name), '\n')
    for counter in range(MIN_ROUND_NUMBER, WIN_COUNTER + 1):
        result, question = game.ask_question()
        print("Question: {}".format(question))
        answer = prompt.string('Your answer: ')
        if brain_games.cli.is_correct_answer(result, answer):
            print('Correct!')
        else:
            brain_games.cli.print_wrong_message(result, answer, name)
            break
        if counter == WIN_COUNTER:
            print('Congratulations, {}'.format(name))
