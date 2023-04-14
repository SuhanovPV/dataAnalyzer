import re

import pandas.core


def normalize_phone(df: pandas.core.frame.DataFrame):
    return df['phone'].apply(lambda x: re.sub(r'\D+', '', str(x)))


def remove_duplicates(df: pandas.core.frame.DataFrame):
    return df.drop_duplicates(['phone'], keep='last')
