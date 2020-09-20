import brain_games.cli
import brain_games.gcd


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.gcd.gcd(name)


if __name__ == '__main__':
    main()
