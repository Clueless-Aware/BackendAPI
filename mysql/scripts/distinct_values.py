import pandas as pd


def load():
    return pd.read_csv('../data/catalog.csv'), pd.read_csv('../data/bio_catalog.csv')


def main():
    artwork_df, artist_df = load()
    print('------------------------------------------------------')

    print('\nUnique professions:')
    print(artist_df['PROFESSION'].unique())
    print('\nUnique schools:')
    print(artist_df['SCHOOL'].unique())

    print('------------------------------------------------------')

    print('\nUnique techniques:')
    print(artwork_df['TECHNIQUE'].unique())
    print('\nUnique locations:')
    print(artwork_df['LOCATION'].unique())
    print('\nUnique forms:')
    print(artwork_df['FORM'].unique())
    print('\nUnique types:')
    print(artwork_df['TYPE'].unique())
    print('\nUnique timeframes:')
    print(artwork_df['TIMEFRAME'].unique())

    print('------------------------------------------------------')


if __name__ == "__main__":
    main()
