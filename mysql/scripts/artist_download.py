import pandas as pd
import requests


def save(df):
    df.to_csv('../data/bio_catalog.csv', header=True, index=False)


def update_url(name):
    new_url = f'images/artists/{name}.jpg'
    return new_url


def download_image(artist_name, url):
    print(f'{artist_name} at {url}')
    portrait_data = requests.get(url).content
    with open(f'../../artApi/images/artists/{artist_name}.jpg', 'wb') as handler:
        handler.write(portrait_data)
    return


def load_data():
    return pd.read_csv('../data/bio_catalog.csv')


def main():
    df = load_data()
    print('init) ------ Load data')

    print(f'------ Starting the download of {df.size} images')
    df[['ARTIST', 'portrait']].apply(lambda artist: download_image(artist['ARTIST'], artist['portrait']), axis=1)

    df['portrait'] = df['ARTIST'].apply(update_url)
    print(df['portrait'])

    save(df)
    print('end) ------ Saving dataframe')


if __name__ == "__main__":
    main()
