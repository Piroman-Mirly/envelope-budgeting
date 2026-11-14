
from db.models import init_db


def main():
    init_db()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Завершение работы')
