import brain_games.game_engine
import brain_games.games.progression


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?', '\n')
    brain_games.game_engine.game_start(brain_games.games.progression)


if __name__ == '__main__':
    main()
