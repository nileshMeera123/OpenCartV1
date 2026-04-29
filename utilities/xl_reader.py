import pandas as pd
import os


def read_xl_data_to_list():
    """

    :return:
    """
    test_data_path = os.path.join(os.path.abspath(os.curdir), "testdata", "login_data.xlsx")
    df = pd.read_excel(test_data_path)
    return df.values.tolist()


