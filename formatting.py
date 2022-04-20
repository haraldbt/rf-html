import pandas as pd


def format_df(
        df: pd.DataFrame,
        label_names: dict[str, str],
        label_formats: dict[str, str]
) -> pd.DataFrame:
    number_labels = {key: label_names[key] for key in ('price', 'abv', 'volume')}
    df = process_numbers(df, **number_labels)

    formats = {label_names[key]: val for key, val in label_formats.items()}
    df = apply_format(df, formats)
    return df


def process_numbers(df: pd.DataFrame, price: str, abv: str, volume: str) -> pd.DataFrame:
    df = df.copy()
    df[price] = df[price].apply(round)
    #df[abv] = (df[abv] * 100).apply(round, ndigits=1)
    df[volume] = (df[volume] * 100).apply(round)
    return df


def apply_format(df: pd.DataFrame, formats: dict[str, str]) -> pd.DataFrame:
    df = df.copy()
    for label, format_string in formats.items():
        df[label] = df[label].apply(format_string.format)
    return df


def apply(df: pd.DataFrame, funcs):
    df = df.copy()
    for label, func in funcs.items():
        df[label] = df[label].apply(func)
    return df


if __name__ == '__main__':
    label_names = {
        'volume': 'Størrelse',
        'abv': 'ABV',
        'price': 'Eksternpris',
        'origin': 'Land',
        'category': 'Kategori',
        'product_name': 'Vare'
    }
    label_formats = {
        'abv': '{:.1%}',
        'volume': '{:d}cl',
        'price': 'kr {:d},-'
    }

    file = 'Meny-RF-V22.xlsx'
    data = pd.read_excel(file)
    on_menu = 'Til salg'
    mask = data[on_menu].notna()
    df = data[mask][label_names.values()]

    result = format_df(df, label_names=label_names, label_formats=label_formats)
    with open('out.html', 'w') as out:
        out.write(result.to_html())