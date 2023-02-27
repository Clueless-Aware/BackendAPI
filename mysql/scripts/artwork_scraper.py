import pandas as pd
import requests
from lxml import html


def scrape(artwork_url):
    # Request the page
    page = requests.get(artwork_url)

    # Parsing the elements to a tree
    tree = html.fromstring(page.content)

    # Get elements using XPath

    # Artwork high quality url
    image_url = tree.xpath('/html/body/table[2]/tr[1]/td[1]/a/@href')

    complete_url = '-'
    try:
        complete_url = 'https://www.wga.hu' + image_url[0]
    except Exception as e:
        print(f'Missing image url {e}')
    # Image description
    desc = tree.xpath(
        '/html/body/table[2]/tr[2]/td/p/text()')

    if desc is None:
        print('No biography found...')
        return ['', complete_url]
    complete_desc = ''

    for paragraph in desc:
        complete_desc += paragraph

    complete_desc = complete_desc.rstrip().lstrip()

    return [complete_desc, complete_url]


def save(df, descriptions):
    pd.concat([df, descriptions], axis=1).to_csv(
        '../data/output.csv', header=True, index=False)
    # print(pd.read_csv('output.csv').size)


def generate_urls():
    # 4634 - 4636
    # 1519
    return pd.read_csv('../data/catalog.csv')


def main():
    df = generate_urls()
    descriptions = pd.DataFrame(columns=['description', 'image_url'])

    index_urls = df['URL'].values
    size = len(index_urls)
    print(f'Generated a total of {size} urls')

    print(f'Starting the download!')
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
        print(f'Successfully download all {size} elements!')

    df.drop(columns=['BORN-DIED', 'SCHOOL', 'URL'], inplace=True)

    save(df, descriptions)

    print(f'Dropped columns and merged the two dataframes')


if __name__ == "__main__":
    main()
