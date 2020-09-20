import brain_games.cli
import brain_games.check_even


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.check_even.even(name)


if __name__ == '__main__':
    main()
