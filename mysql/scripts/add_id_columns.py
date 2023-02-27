import pandas as pd


def add_id(name, artists):
    mask = (artists['ARTIST'] == name)
    artists_valid = artists[mask]

    try:
        return artists_valid['id'].values[0]
    except IndexError:
        return '-1'


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
    artworks = pd.read_csv('../data/catalog.csv')
    artists = pd.read_csv('../data/bio_catalog.csv')

    print('1) ------- Loading')

    artists['id'] = range(0, len(artists.values))

    print('2) ------- Adding id to artist')

    artworks['artist id'] = artworks['AUTHOR'].apply(lambda x: add_id(x, artists))

    print('3) ------- Adding artist id to artwork')

    save(artists, artworks)

    print('4) ----- Saving')

    calculate_mismatch(artworks, artists)
    print('5) Calculate mismatch between artists and artwork')


if __name__ == "__main__":
    main()
