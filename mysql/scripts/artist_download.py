import pandas as pd


def save(df):
    df.to_csv('try.csv', header=True, index=False)


def update_url(name):
    new_url = f'images/artists/{name}.jpg'
    return new_url


def download_image():
    return


def load_data():
    return pd.read_csv('../data/bio_catalog.csv')


def main():
    df = load_data()
    print('int) ------ Load data')

    cont = 0
    df['portrait'] = df['ARTIST'].apply(update_url)
    print(df['portrait'])

    save(df)
    print('end) ------ Saving dataframe')


if __name__ == "__main__":
    main()
