import brain_games.cli
import brain_games.calc


def main():
    print('Welcome to the Brain Games!', '\n')
    brain_games.cli.welcome_user()


def calc():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.calc.calc(name)


if __name__ == '__main__':
    main()
