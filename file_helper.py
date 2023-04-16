import pandas as pd
import os

import pandas.core.frame

from data_handler import normalize_phone, remove_duplicates


def get_init_path():
    return os.path.join(os.environ['USERPROFILE'], 'Desktop')


def convert_path(path: str, size: int):
    new_path = os.path.normpath(path)
    return trim_path(new_path, size)


def trim_path(path: str, size: int):
    if len(path) > size:
        path = path[0:3] + '...' + path[-size + 3:]
    return path


def save_to_file(df: pandas.core.frame.DataFrame, path: str):
    df.to_excel(path, index=False)


def get_path_to_output(path: str):
    dir_name, file_name = os.path.split(path)
    name, ext = os.path.splitext(file_name)
    new_name = name + '_no_duplicates' + ext
    new_path = os.path.join(dir_name, new_name)
    return new_path


def create_file_with_unique_users(path: str):
    users = pd.read_excel(path)
    # TODO: выяснить, надо ли преобразоввывать телефон
    users['phone'] = normalize_phone(users)
    users = remove_duplicates(users)
    path_to_output_file = get_path_to_output(path)
    save_to_file(users, path_to_output_file)


if __name__ == '__main__':
    get_init_path()
