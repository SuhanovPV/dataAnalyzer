import pandas as pd
import os

import pandas.core.frame

from data_handler import normalize_phone, remove_duplicates


def get_init_path():
    return os.path.join(os.environ['USERPROFILE'], 'Desktop')


def path_to_win_format(path: str):
    return os.path.normpath(path)


def convert_path(path: str, size: int):
    return trim_path(path_to_win_format(path), size)


# TODO Добавить обрезание пути по пути пользователя, если файлы находятся на диске C. Иначе обрезать по длинне, если требуется
def trim_path(path: str, size: int):
    path = path[0:3] + '...' + path[6 + size:]
    return path


def get_file_name(path: str):
    return os.path.split(path)[1]


def save_to_file(df: pandas.core.frame.DataFrame, path: str):
    df.to_excel(path, index=False)


def get_path_to_output(path: str):
    dir_name, file_name = os.path.split(path)
    name, ext = os.path.splitext(file_name)
    new_name = name + '_tmp' + ext
    new_path = os.path.join(dir_name, new_name)
    return new_path


def create_file_with_unique_users(path: str):
    users = pd.read_excel(path)
    # TODO: выяснить, надо ли преобразоввывать телефон
    users['phone'] = normalize_phone(users)
    users = remove_duplicates(users)
    path_to_output_file = get_path_to_output(path)
    save_to_file(users, path_to_output_file)
    return path_to_output_file


def add_files_to_list(fileset: set, files: tuple):
    return fileset.union(files)


def open_file_in_excel(file):
    os.startfile(file)


if __name__ == '__main__':
    add_files_to_list('C:/Users/Pavel.Sukhanov/Desktop/dir')
