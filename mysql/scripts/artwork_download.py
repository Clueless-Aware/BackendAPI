import pandas as pd
import requests


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

    print('Finshed scraping!')


if __name__ == "__main__":
    main()
