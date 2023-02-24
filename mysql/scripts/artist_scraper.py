import pandas as pd
import requests
from lxml import html


def scrape(url):
    # Request the page
    page = requests.get(url)

    # Parsing the elements to a tree
    tree = html.fromstring(page.content)

    # Get elements using XPath

    # Artist portrait
    image_url = tree.xpath('/html/body/center/table/tr/td/img/@src')
    try:
        image_url[0] = 'https://www.wga.hu' + image_url[0]
    except Exception as e:
        print(f'Missing image url {e}')
        image_url[0] = '-'

    # Artist biography
    bio = tree.xpath(
        '/html/body/center/table/tr/td/p')
    if bio is None:
        print('No biography found...')
        return ['', image_url[0]]
    complete_bio = ''

    for paragraph in bio:
        complete_bio += paragraph.text_content()

    complete_bio = complete_bio.rstrip().lstrip()

    return [complete_bio, image_url[0]]


def generate_urls():
    return pd.read_csv('../data/bio_catalog.csv')


def main():
    df = generate_urls()
    index_urls = df['URL'].values
    size = len(index_urls)
    print(f"init) --------- Generated a total of {size} urls")
    descriptions = pd.DataFrame(columns=['description', 'portrait'])

    cont = 0
    try:
        for url in index_urls:
            print(f'{cont}/{size}) ------- Downloading bio for {url}')
            descriptions.loc[len(descriptions)] = scrape(url)
            cont += 1
    except KeyboardInterrupt:
        print(
            f'Stopping scraping... I was working on element {cont}/{size}')
    except Exception as e:
        print(f'Generic exception {e} - {e.__traceback__} - {e.__cause__}')
    else:
        print('All went well!')

    print('closing) --------- Saving new dataframe to a csv file')
    df.drop('URL', axis=1, inplace=True)
    pd.concat([df, descriptions], axis=1).to_csv(
        'test.csv', header=True, index=False)


if __name__ == "__main__":
    main()
