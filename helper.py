import pandas as pd
import re

import pandas.core.frame


def convert_path(path: str, size: int):
    new_path = convert_path_to_win_format(path)
    return trim_path(new_path, size)


def convert_path_to_win_format(path):
    return path.replace('/', '\\')


def trim_path(path: str, size: int):
    if len(path) > size:
        path = path[0:3] + '...' + path[-size + 3:]
    return path


def normalize_phone(df: pandas.core.frame.DataFrame):
    return df['phone'].apply(lambda x: re.sub(r'\D+', '', str(x)))


def remove_duplicates(df: pandas.core.frame.DataFrame):
    return df.drop_duplicates(['phone'], keep='last')


def save_to_file(df: pandas.core.frame.DataFrame):
    df.to_excel('C:/Users/Pavel.Sukhanov/Desktop/testUsers_mod.xlsx', index=False)


def create_file_with_unique_users(path: str):
    path = 'C:/Users/Pavel.Sukhanov/Desktop/testUsers.xlsx'
    users = pd.read_excel(path)
    # TODO: выяснить, надо ли преобразоввывать телефон
    users['phone'] = normalize_phone(users)
    users = remove_duplicates(users)
    save_to_file(users)


if __name__ == '__main__':
    create_file_with_unique_users('')
