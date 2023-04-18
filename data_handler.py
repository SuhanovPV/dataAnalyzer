import re

import pandas.core.frame as frame


def normalize_phone(df: frame.DataFrame):
    return df['phone'].apply(lambda x: re.sub(r'\D+', '', str(x)))


def remove_duplicates(df: frame.DataFrame):
    return df.drop_duplicates(['phone'], keep='last')
