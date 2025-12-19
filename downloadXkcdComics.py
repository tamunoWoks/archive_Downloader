# downloadXkcdComics.py - Downloads XKCD comics

import requests
import os
import bs4
import time

BASE_URL = 'https://xkcd.com'
url = BASE_URL  # Starting URL

os.makedirs('xkcd', exist_ok=True)  # Store comics in ./xkcd

num_downloads = 0
MAX_DOWNLOADS = 20

while not url.endswith('#') and num_downloads < MAX_DOWNLOADS:
    # Download the page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the comic image
    comic_elem = soup.select('#comic img')
    if not comic_elem:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')

        # Download the image
        print(f'Downloading image {comic_url}...')
        image_res = requests.get(comic_url)
        image_res.raise_for_status()

        # Save the image
        image_path = os.path.join('xkcd', os.path.basename(comic_url))
        with open(image_path, 'wb') as image_file:
            for chunk in image_res.iter_content(100000):
                image_file.write(chunk)

    # Get the Previous Comic link
    prev_link = soup.select_one('a[rel="prev"]')
    if prev_link:
        url = BASE_URL + prev_link.get('href')
    else:
        break

    num_downloads += 1
    time.sleep(1)  # Pause so we don't hammer the web server

print('Done.')
