def convert_path(path: str, size: int):
    new_path = convert_path_to_win_format(path)
    return trim_path(new_path, size)

def convert_path_to_win_format(path):
    return path.replace('/', '\\')

def trim_path(path: str, size: int):
    if len(path) > size:
        path = path[0:3] + '...' + path[-size + 3:]
    return path
