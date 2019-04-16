import config as conf


def get_directory(data_type: str, data_attr='data'):
    """
    Dizin verisini döndürür
    :param data_type: Veri tipi in, out, bg
    :param data_attr: Veri özelliği data, test
    :return: Dizin yolu
    """

    dir_path: str = ""

    if data_attr != 'test':
        prefix = conf.BASE_DATA_DIR + "/"
    else:
        prefix = conf.BASE_TEST_DIR + "/"

    if data_type == 'in':
        dir_path = prefix + "inputs"
    elif data_type == 'out':
        dir_path = prefix + "outputs"
    elif data_type == 'bg':
        dir_path = prefix + "backgrounds"

    return dir_path


def join_path(file_name, path):
    return path + "/" + file_name


def get_file_path(file_name: str, data_type: str, data_attr: str = 'data'):
    return join_path(file_name, get_directory(data_type, data_attr))
