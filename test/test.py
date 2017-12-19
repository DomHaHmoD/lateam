import os


def get_current_dir(current_file):
    return os.path.dirname(os.path.abspath(current_file))


def get_data_dir(current_file):
    return os.path.join(get_current_dir(current_file), "src")


DATA_DIR = get_data_dir(__file__)

print(DATA_DIR)
