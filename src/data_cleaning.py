import pandas as pd
import os

def clean_data(file_path):

    df = pd.read_excel(file_path)

    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    df.drop_duplicates(inplace=True)

    df.ffill(inplace=True)

    return df


def save_clean_data(df, path):

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df.to_csv(path, index=False)