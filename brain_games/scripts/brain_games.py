from brain_games.cli import welcome_user


def greeting():
    print("Welcome to the Brain Games!")


def rules_games(game_name):
    if game_name == 'even':
        return 'Answer "yes" if number even otherwise answer "no".\n'


def main():
    greeting()
    welcome_user()


if __name__ == "__main__":
    main()
