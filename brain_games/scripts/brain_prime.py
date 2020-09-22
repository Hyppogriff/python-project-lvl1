import brain_games.cli
import brain_games.prime


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".',
          '\n')
    name = brain_games.cli.welcome_user()
    brain_games.prime.prime(name)


if __name__ == '__main__':
    main()
