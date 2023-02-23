import copy

import requests
from bs4 import BeautifulSoup


def create_urls(url):
    # string.ascii_lowercase
    urls = []
    for letter in ['q']:
        urls.append(url + letter + "/")
    return urls


def get_anchors_from_html(_url):
    # get the source code of the page
    data = requests.get(_url)
    html = BeautifulSoup(data.text, 'html.parser')
    # parse it and select all the anchor elements
    anchors = html.select('a')

    return anchors


def scrap(current_url):
    pattern = ">[a-z]<"

    anchors = get_anchors_from_html(current_url)
    print("3) --------- Gathering all anchors for all artists in letter")

    artists = parse_elements(anchors, pattern)
    print("4) --------- Parsing anchors into an artist name")

    # Stitch together the artists with the letter.
    image_names = []
    for name in artists:
        image_names.append(current_url + name + "/")
    artist_links = copy.deepcopy(image_names)

    print("5) --------- Converting artists names to working urls")

    # look for images files under each artist
    resources = []

    for artist_url in image_names:
        print(f'6) --------- Gathering image anchors for {artist_url}')
        files = get_anchors_from_html(artist_url)
        resources.append(files)

    print(f"7) --------- Gathered anchor elements from all artists")

    # remove html tag from elements
    image_names.clear()
    for e in resources:
        image_names.append(parse_elements(e, pattern))
    print("8) --------- Parsed all artist anchors to strings")

    print(f"8.5) --------- Looking for subdirectories")
    # i = 0
    # for artist_images in image_names:
    # i = i + 1
    # for image_name in artist_images:
    # if not image_name.endswith('.jpg'):
    # print(f'I have found a subdirectory: {image_name} - {artist_links[i]}')

    file_url = []

    # Stitch the Artist link with the resources

    for i in range(len(artist_links)):
        for j in range(len(image_names[i])):
            file_url.append(artist_links[i] + image_names[i][j])

    print("9) --------- Stitching together image url with artist")

    write(file_url)
    print("10) --------- Write to a txt file")


def parse_elements(elements, _pattern):
    results = []

    for e in elements:
        e = e.string
        # get the first element as a string
        if e not in ['info.dat', '..']:
            results.append(e)

    return results


def write(out):
    with open("output.txt", "w") as txt_file:
        for line in out:
            txt_file.write("".join(line) + "\n")


def main():
    base_url = 'https://www.wga.hu/art/'

    index_urls = create_urls(base_url)
    print("1) --------- Generating urls")

    for _url in index_urls:
        print(f'2) --------- Working on {_url}')
        scrap(_url)


if __name__ == "__main__":
    main()
