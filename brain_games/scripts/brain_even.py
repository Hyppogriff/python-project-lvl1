import brain_games.game_engine
import brain_games.games.check_even


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".', '\n')
    brain_games.game_engine.game_start(brain_games.games.check_even)


if __name__ == '__main__':
    main()
