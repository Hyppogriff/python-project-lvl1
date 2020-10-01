import brain_games.game_engine
import brain_games.games.gcd


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.', '\n')
    brain_games.game_engine.game_start(brain_games.games.gcd)


if __name__ == '__main__':
    main()
