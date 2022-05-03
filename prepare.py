import pandas as pd


def prepare_df(df: pd.DataFrame, on_menu: str, labels: dict[str, str]) -> pd.DataFrame:
    df = df.copy()
    mask = df.loc[:, on_menu].notna()
    columns = list(labels.values())
    df = df.loc[mask, columns]
    df.set_index(labels['product_name'], inplace=True)
    return df


def format_df(df: pd.DataFrame, labels: dict[str, str], formats: dict[str, str]) -> pd.DataFrame:
    df = df.copy()

    # Replace na
    df.loc[:, labels['abv']].fillna(0, inplace=True)
    df.loc[:, labels['origin']].fillna(str(), inplace=True)

    # Round numbers
    price = labels['price']
    volume = labels['volume']
    df.loc[:, price] = df.loc[:, price].apply(round)
    df.loc[:, volume] = (df.loc[:, volume] * 100).apply(round)

    # Format numbers as strings
    for key, format_string in formats.items():
        label = labels[key]
        df.loc[:, label] = df.loc[:, label].apply(format_string.format)

    return df