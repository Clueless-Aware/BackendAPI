import pandas as pd


def update_url(art_id):
    new_url = f'images/artworks/{art_id}.jpg'
    return new_url


def load():
    return pd.read_csv('../data/catalog.csv')


def save_urls(df):
    df.to_csv('../data/urls.csv', header=True, index=False)


def save(df):
    df.to_csv('./new.csv', header=True, index=False)


def main():
    print('Acquiring urls')
    df = load()

    print('Saving urls to new dataframe')
    save_urls(df['image_url'])

    print('Updating urls to point to local')
    df['image url'] = df.apply(lambda x: update_url(x.name), axis=1)
    df.drop(columns=['image_url'], inplace=True)
    # print(df['image url'])

    print('Saving new data frame')
    save(df)


if __name__ == "__main__":
    main()
