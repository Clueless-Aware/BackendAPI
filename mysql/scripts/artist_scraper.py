import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def scrape(url):
    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    with driver:
        driver.get(url)
        # find element by xpath
        frame = driver.find_element(By.XPATH, '/html/frameset/frame[2]')

        driver.switch_to.frame(frame)
        desc = ''
        # TODO: not found
        paragraphs = driver.find_elements(By.CSS_SELECTOR, 'td p')
        for paragraph in paragraphs:
            desc += (paragraph.text + '\n')

        img_url = driver.find_element(
            By.XPATH, '/html/body/center/table/tbody/tr[2]/td/img').get_attribute("src")
        # download file somewhere set a new name/path

        # TODO: fill the column[description,img_url]

    return [desc, img_url]


def generate_urls():
    return pd.read_csv('../data/bio_catalog.csv', nrows=50)


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
