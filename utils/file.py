from utils import path


def save_file(file, file_name, data_type='out', data_attr='data'):
    file.save(path.get_file_path(file_name, data_type, data_attr))
