import brain_games.cli


def run_game(game):
    brain_games.cli.greeting()
    print(game.show_description(), '\n')
    name = brain_games.cli.welcome_user()
    win_counter = 3
    for counter in range(1, win_counter + 1):
        result, question = game.ask_question()
        print(question)
        answer = brain_games.cli.get_answer(game)
        if brain_games.cli.is_correct_answer(result, answer):
            brain_games.cli.print_correct_message()
        else:
            brain_games.cli.print_wrong_message(result, answer, name)
            break
        brain_games.cli.check_win_counter(counter, win_counter, name)
