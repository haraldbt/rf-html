from .prepare import prepare_df, format_df
import pandas as pd

def main():
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

    df = prepare_df(data, on_menu=on_menu, labels=label_names)
    df = format_df(df, labels=label_names, formats=label_formats)
    grouped = df.groupby(label_names['category'])
    for category, products in grouped:
        print(category)
        print(products)
        print()


if __name__ == '__main__':
    main()