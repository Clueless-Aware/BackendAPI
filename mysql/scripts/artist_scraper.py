import pandas as pd
import requests
from lxml import html


def scrape(url):

    # Request the page
    page = requests.get(url)

    # Parsing the page
    tree = html.fromstring(page.content)
    # tree = cleaner.clean_html(page.content)

    # Get element using XPath
    image_url = tree.xpath('/html/body/center/table/tr/td/img/@src')
    # print(image_url[0])

    bio = tree.xpath(
        '/html/body/center/table/tr/td/p')
    completeBio = ''

    for paragraph in bio:
        completeBio += paragraph.text_content()

    completeBio = completeBio.rstrip().lstrip()
    # print(f'Complete bio: {completeBio}')

    return [completeBio, image_url[0]]


def generate_urls():
    return pd.read_csv('../data/bio_catalog.csv', nrows=100)


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

    print('closing) --------- Saving new dataframe to a csv file')
    df.drop('URL', axis=1, inplace=True)
    pd.concat([df, descriptions], axis=1).to_csv(
        'test.csv', header=True, index=False)


if __name__ == "__main__":
    main()
