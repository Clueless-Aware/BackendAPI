import pandas as pd
import requests


def download_image(artwork_id, url):
    print(f'Id {artwork_id} at {url}')

    try:
        portrait_data = requests.get(url).content
    except Exception as e:
        print(f'Warning missing url at id f{artwork_id} - {e.__cause__}')

    with open(f'../../artApi/images/artworks/{artwork_id}.jpg', 'wb') as handler:
        handler.write(portrait_data)
    return


def load_data():
    return pd.read_csv('../data/urls.csv', nrows=100)


def main():
    df = load_data()
    print('init) ------ Load data')

    print(f'------ Starting the download of {len(df)} images')

    try:
        df.apply(lambda art: download_image(
            art.name, art['image_url']), axis=1)
    except KeyboardInterrupt:
        print('Stopping scraping...')
    except Exception as e:
        print(
            f'Generic exception while downloading images: {e.__cause__} - {e.__str__()}')

    print('Finished scraping!')


if __name__ == "__main__":
    main()
