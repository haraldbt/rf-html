from prepare import prepare_df, format_df
import pandas as pd


def main():
    df = prepare_file()
    grouped = df.groupby('category')
    for category, products in grouped:
        print(category)
        print(products)
        print()

def prepare_file():
    label_names = {
        'volume': 'Størrelse',
        'abv': 'ABV',
        'price': 'Eksternpris',
        'origin': 'Land',
        'category': 'Kategori',
        'product_name': 'Vare',
        'on_menu': 'Til salg'
    }
    label_formats = {
        'abv': '{:.1%}',
        'volume': '{:d}cl',
        'price': 'kr {:d},-'
    }

    file = 'Meny-RF-V22.xlsx'
    data = pd.read_excel(file)

    df = prepare_df(data, labels=label_names)
    df = format_df(df, formats=label_formats)
    return df


if __name__ == '__main__':
    main()