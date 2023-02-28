import pandas as pd


def add_id(name, artists):
    mask = (artists['ARTIST'] == name)
    artists_valid = artists[mask]

    try:
        return artists_valid.index[0] + 1
    except IndexError:
        return '1'


def calculate_mismatch(artworks, artists):
    mismatch = []

    for artwork in artworks['AUTHOR'].unique():
        if artwork not in artists['ARTIST'].values:
            mismatch.append(artwork)

    print(mismatch, f'\nThe are currently {len(mismatch)} mismatches')


def save(artist, artworks):
    artist.to_csv('new_artists.csv', header=True, index=False)
    artworks.to_csv('new_artworks.csv', header=True, index=False)


def main():
    print('1) ------- Loading')

    artworks = pd.read_csv('../data/catalog.csv')
    artists = pd.read_csv('../data/bio_catalog.csv')

    print('2) ------- Remove id from artist')

    try:
        artists.drop(columns=['id'], inplace=True)
    except KeyError:
        print('2.5) ------- Id table already removed')

    print('3) ------- Adding artist id to artwork')

    artworks['artist id'] = artworks['AUTHOR'].apply(lambda x: add_id(x, artists))

    print('4) ----- Saving')

    save(artists, artworks)

    print('5) Calculating mismatch between artists and artwork')

    calculate_mismatch(artworks, artists)


if __name__ == "__main__":
    main()
