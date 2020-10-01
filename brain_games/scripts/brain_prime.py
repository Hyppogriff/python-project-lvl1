import brain_games.game_engine
import brain_games.games.prime


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".',
          '\n')
    brain_games.game_engine.game_start(brain_games.games.prime)


if __name__ == '__main__':
    main()
