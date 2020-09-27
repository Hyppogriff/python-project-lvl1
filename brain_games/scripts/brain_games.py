import brain_games.cli
import brain_games.calc
import brain_games.check_even
import brain_games.gcd
import brain_games.prime
import brain_games.progression


def main():
    print('Welcome to the Brain Games!', '\n')
    brain_games.cli.welcome_user()


def calc():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.calc.calc(name)


def even():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.check_even.even(name)


def gcd():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.gcd.gcd(name)


def prime():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".',
          '\n')
    name = brain_games.cli.welcome_user()
    brain_games.prime.prime(name)


def progression():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?', '\n')
    name = brain_games.cli.welcome_user()
    brain_games.progression.progression(name)


if __name__ == '__main__':
    main()
