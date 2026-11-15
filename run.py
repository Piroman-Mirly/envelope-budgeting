from db import models
from db.models import init_db
from ui.app import App


def main():
    init_db()
    App().mainloop()
    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Завершение работы')
