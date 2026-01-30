import configparser
import os


def setup():
    config = configparser.ConfigParser()
    # config.read('config.ini')
    config = configparser.ConfigParser()
    project_root = os.getcwd()  # D:\OpenCartV1
    config_path = os.path.join(
        project_root,
        'configurations',
        'config.ini'
    )
    # print(config_path)
    config.read(config_path)
    return config



def get_username():
    # breakpoint()
    return setup().get('common','username')

def get_password():
    return setup().get('common','password')

def get_base_url():
    return setup().get('common','baseUrl')


# print(get_base_url())
