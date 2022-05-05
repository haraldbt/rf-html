import pandas as pd
import numpy as np


def prepare_df(df: pd.DataFrame, labels: dict[str, str]) -> pd.DataFrame:
    df = df.copy()

    mask = df.loc[:, labels['on_menu']].notna()
    new_labels = {val: key for key, val in labels.items()}
    columns_to_keep = list(new_labels.values())
    columns_to_keep.remove('on_menu')

    df.rename(columns=new_labels, inplace=True)
    df = df.loc[mask, columns_to_keep]
    df.set_index('product_name', inplace=True)

    return df


def format_df(df: pd.DataFrame, formats: dict[str, str]) -> pd.DataFrame:
    df = df.copy()

    # Replace na
    df.loc[:, 'abv'].fillna(0, inplace=True)
    df.loc[:, 'origin'].fillna(str(), inplace=True)

    df.loc[:, 'price'] = df.loc[:, 'price'].apply(np.floor).astype('int')
    # Convert from liters to centiliters
    df.loc[:, 'volume'] = (df.loc[:, 'volume'] * 100).apply(np.floor).astype('int')

    # Format numbers as strings
    for label, format_string in formats.items():
        df.loc[:, label] = df.loc[:, label].apply(format_string.format)

    return df