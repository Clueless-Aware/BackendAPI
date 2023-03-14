from os.path import exists

import pandas as pd


def in_file_system(path):
    return not (exists(f'../../artApi/{path}'))


def load():
    return pd.read_csv('../data/catalog.csv'), pd.read_csv('../data/bio_catalog.csv')


def main():
    artwork_df, artist_df = load()

    # artwork_df['image url'].where(lambda x: not exists(f'../../artApi/{x}'))
    for url in artwork_df['image url']:
        if in_file_system(url):
            print('Missing image at: ' + url)
    # artwork_df['image url'].where(in_file_system)


if __name__ == "__main__":
    main()
