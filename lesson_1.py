import os
import shutil
from datetime import datetime


def archive():
    # Автонейминг архивов
    auto_name_archive = datetime.now().strftime('%d.%m.%Y-%H.%M.%S')

    # создание архивации папки test
    shutil.make_archive(f'all_archives/{auto_name_archive}', 'zip', 'test')

    # создадим список файлов в папке all_archives
    list_dir = os.listdir('all_archives')

    # соберем у всех файлов полный путь
    full_path_all_archives = [os.path.join('all_archives', i) for i in list_dir]

    # удаляем все архивы, кроме последних пяти
    for i in full_path_all_archives[:-5]:
        os.unlink(i)


archive()
