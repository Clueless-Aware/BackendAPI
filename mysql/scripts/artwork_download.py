import pandas as pd
import requests


def save(df):
    df.to_csv('../updated_artwork.csv', header=True, index=False)


def update_url(id):
    new_url = f'images/artworks/{id}.jpg'
    return new_url


def download_image(id, url):
    print(f'Id {id} at {url}')
    portrait_data = requests.get(url).content
    with open(f'../../artApi/images/artworks/{id}.jpg', 'wb') as handler:
        handler.write(portrait_data)
    return


def load_data():
    return pd.read_csv('../data/catalog.csv', nrows=100)


def main():
    df = load_data()
    print('init) ------ Load data')

    print(f'------ Starting the download of {len(df)} images')

    df.apply(lambda art: download_image(
        art.name, art['image_url']), axis=1)

    df['image url'] = df['ARTIST'].apply(lambda x: update_url(x.name))
    # print(df['image url'])
    print('Updating dataframe to point to the correct url')

    # save(df)
    print('end) ------ Saving dataframe')


if __name__ == "__main__":
    main()
