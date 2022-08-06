from main import prepare_file
from pprint import pprint
from chevron import render
import pandas as pd
from collections.abc import Iterator
import toml


def structure_df(df: pd.DataFrame, labels: dict[str, str]) -> dict[str, Iterator[tuple]]:
    result = []
    canon_labels = 'product_name volume abv price origin'.split()
    template_labels = [labels[canon_label] for canon_label in canon_labels]
    df = df.copy()
    for category, sub_df in df.groupby('category'):
        sub_df.drop(columns='category', inplace=True)
        products = (dict(zip(template_labels, row)) for row in sub_df.itertuples(name=None))
        products = [{'products': product} for product in products]

        result.append({category: products})
    return {'categories': result}


if __name__ == '__main__':
    with open('config.toml') as f:
        config = toml.loads(f.read())
    df = prepare_file()
    structured = structure_df(df, config['template'])
    # data = ({category: {'products': rows}} for category, rows in structured.items())
    # data = {'categories': {'products': {'name': 'hei', 'size': 2, 'abv': 3, 'country': 5, 'price': 7}}}
    with open('template.ms') as f:
        template = f.read()
    with open('out.html', 'w') as out:
        out.write(render(template=template, data=structured))

    pprint(structured)