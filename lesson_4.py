import functools
import shutil, os, time
from datetime import datetime
import logging


def dec_count(func):
    # @functools.wraps(func)
    def wrapper(*args):
        """Decorator count"""
        wrapper.count += 1
        func(*args)
        print(f'The func was called {wrapper.count} times')

    wrapper.count = 0
    return wrapper


def dec_time(func):
    @functools.wraps(func)
    def wrapper_time(*args):
        """Decorator count time"""

        get_time = time.time()
        func(*args)
        print(f'The func completed the task in {time.time() - get_time} seconds')

    return wrapper_time


def dec_log(func):
    @functools.wraps(func)
    def wrapper_logging(*args):
        """Decorator logging"""

        # Создадим имя логера
        name_logger = func.__name__

        # Создадим именнованый логгер
        logger = logging.getLogger(name_logger)

        # Уровень логгера
        logger.setLevel(logging.INFO)

        # Open the logfile for
        # writing
        # Обратчик файлов
        file_handler = logging.FileHandler(f'{name_logger}.log')
        time_log = time.time()

        fmt = str(time_log) + ' - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info("Function call: %s" % name_logger)
        a, b = args
        print(a, b)
        func(*args)

        result = f'Created {a} archives with a period of {b} seconds'
        logger.info(result)
        logger.info(f'Total time: {time.time() - time_log}')
        print(args)

    return wrapper_logging


@dec_log
@dec_time
@dec_count
def archive(count_digit, sec_count, count=0):
    """Backups data"""

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
    print(dec_log.__doc__)
    print(dec_time.__doc__)
    print(dec_count.__doc__)
    print(archive.__doc__)
