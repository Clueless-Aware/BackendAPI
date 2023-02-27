import pandas as pd


def add_id(name, artists):
    cont = 0
    for artist in artists:
        if name == artist:
            return cont
        cont += 1

    return '-1'


def main():
    artworks = pd.read_csv('../data/catalog.csv')
    artists = pd.read_csv('../data/bio_catalog.csv')['ARTIST'].values

    # artworks['artist id'] = artworks['AUTHOR'].apply(lambda x: add_id(x, artists))

    mismatch = []

    for artwork in artworks['AUTHOR'].unique():
        if artwork not in artists:
            mismatch.append(artwork)

    print(mismatch, f'\nThe are currently {len(mismatch)} mismatches')

    # print(artworks['artist id'].to_string())


if __name__ == "__main__":
    main()
