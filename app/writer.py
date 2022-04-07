import os

import pandas as pd


def load_db_table(df: pd.DataFrame, connection, table_name: str, key: str) -> None:
    min_key = df[key].min()
    max_key = df[key].max()
    df.to_sql(table_name, connection, if_exists='append', index=False)
    print(f'Loaded data for {table_name} with in the range of {min_key} and {max_key}')
