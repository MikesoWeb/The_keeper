import os
import shutil
import time
from datetime import datetime


def dec_log(func):
    def wrapper(*args):
        print('Open decorator log')
        a, b = args
        print(a, b)
        print(type(args))
        func(a, b)
        print('Close decorator log')

    return wrapper


def dec_count(func):
    def wrapper(*args):
        """Decorator count"""

        wrapper.count += 1
        func(*args)
        print(f'The func was called {wrapper.count} times')

    wrapper.count = 0
    return wrapper


@dec_log
@dec_count
def archive(count_digit, sec_count, count=0):
    """Выполняет архивацию данных"""
    while count != count_digit:
        # Автонейминг архивов
        auto_name_archive = datetime.now().strftime('%d.%m.%Y-%H.%M.%S')

        # создание архивации папки test
        print(f'Create a new archive {auto_name_archive}')
        shutil.make_archive(f'all_archives/{auto_name_archive}', 'zip', 'test')
        print(f'New archive created {auto_name_archive}')

        # создадим список файлов в папке all_archives
        list_dir = os.listdir('all_archives')

        # соберем у всех файлов полный путь
        full_path_all_archives = [os.path.join('all_archives', i) for i in list_dir]

        for i in full_path_all_archives[:-5]:
            shutil.move(i, 'old_archives')
            print(f'The archive {i} was moved to folder "old_archives"')

        # создадим список файлов в папке old_archives
        list_dir_old_archives = os.listdir('old_archives')

        # соберем у всех файлов полный путь
        full_path_old_archives = [os.path.join('old_archives', j) for j in list_dir_old_archives]

        # удаляем все архивы, кроме последних пяти
        for j in full_path_old_archives[:-10]:
            os.unlink(j)
            print(f'The archive {j} was deleted permanently!')
        time.sleep(sec_count)
        count += 1
        print()


if __name__ == '__main__':
    archive(1, 5)

