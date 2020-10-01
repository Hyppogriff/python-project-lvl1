import brain_games.game_engine
import brain_games.games.calc


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?', '\n')
    brain_games.game_engine.game_start(brain_games.games.calc)


if __name__ == '__main__':
    main()
