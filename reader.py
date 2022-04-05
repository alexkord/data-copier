import os
import pandas as pd


def get_json_reader(BASE_DIR: str, table_name: str, chunksize=1000):
    file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
    fp = f'{BASE_DIR}/{table_name}/{file_name}'
    return pd.read_json(fp, lines=True, chunksize=chunksize)
