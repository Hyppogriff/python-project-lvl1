import brain_games.cli
import brain_games.progression


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.progression.progression(name)


if __name__ == '__main__':
    main()
