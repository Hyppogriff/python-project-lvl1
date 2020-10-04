import brain_games.cli


def run_game(game):
    brain_games.cli.greeting()
    print(game.show_description(), '\n')
    name = brain_games.cli.welcome_user()
    win_counter = 3
    for counter in range(1, win_counter + 1):
        result, answer = game.ask_question()
        if brain_games.cli.is_correct_answer(result, answer):
            print('Correct!')
        else:
            print('\'', answer, '\'', ' is wrong answer ;(. Correct answer \
 was ', '\'', result, '\'', sep='')
            print('Let\'s try again,', name)
            break
    brain_games.cli.check_win_counter(counter, win_counter, name)
