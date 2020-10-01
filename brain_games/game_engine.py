import brain_games.cli


def game_start(game):
    name = brain_games.cli.welcome_user()
    win_counter = 3
    while win_counter > 0:
        result, answer = game.question()
        if brain_games.cli.isResult(result, answer, name):
            win_counter -= 1
        else:
            break
    if win_counter == 0:
        print('Congratulations,', name)
