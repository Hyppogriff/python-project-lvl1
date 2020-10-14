import brain_games.cli


def main():
    print('Welcome to the Brain Games!')
    print('Hello, {}'.format(brain_games.cli.get_user_name()))


if __name__ == '__main__':
    main()
