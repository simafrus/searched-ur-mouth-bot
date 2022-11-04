import os
from main import bot_


def main():
    TOKEN = os.environ.get("TOKEN")
    bot_(TOKEN)


if __name__ == '__main__':
    main()
