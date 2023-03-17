from os.path import exists

import pandas as pd


def in_file_system(path):
    return exists(f'../../artApi/{path}')


def load():
    return pd.read_csv('../data/catalog.csv'), pd.read_csv('../data/bio_catalog.csv')


def save(df):
    df.to_csv('./output/null_images.csv', header=True, index=False)


def main():
    artwork_df, artist_df = load()

    artwork_df['in_file_system'] = artwork_df['image url'].apply(lambda x: in_file_system(x))

    mask = (artwork_df['in_file_system'] == False)
    missing = artwork_df[mask]

    if len(missing) != 0:
        print('Missing images in our DB found!')
        save(missing)
        print('Saved into a csv...')
    else:
        print('DB is complete :)')


if __name__ == "__main__":
    main()
