import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_image(image_url, folder="posters"):
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, os.path.basename(urlparse(image_url).path))

    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {image_url}")

def get_movie_posters(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch Wikipedia page")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="wikitable")
    if not table:
        print("Could not find the table with movie data.")
        return

    for row in table.find_all("tr")[1:]:  # Skip the header row
        link = row.find("a")
        if link and link.get("href"):
            movie_page_url = urljoin(url, link["href"])
            download_poster_from_movie_page(movie_page_url)

def download_poster_from_movie_page(movie_page_url):
    response = requests.get(movie_page_url)
    if response.status_code != 200:
        print(f"Failed to fetch movie page: {movie_page_url}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    infobox = soup.find("table", class_="infobox")
    if not infobox:
        print(f"No infobox found on {movie_page_url}")
        return

    img = infobox.find("img")
    if img and img.get("src"):
        image_url = urljoin("https://en.wikipedia.org", img["src"])
        download_image(image_url)
    else:
        print(f"No poster image found for {movie_page_url}")

if __name__ == "__main__":
    wiki_url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
    get_movie_posters(wiki_url)
