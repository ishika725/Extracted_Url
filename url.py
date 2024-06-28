import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def extract_urls(query, num_results):
    urls = []
    page = 0
    while len(urls) < num_results:
        response = requests.get(f"https://www.google.com/search?q={query}&start={page}")
        if response.status_code != 200:
            print(f"Failed to retrieve search results: {response.status_code}")
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if "arcgis/rest/services" in href:
                urls.append(href.split('&')[0].replace('/url?q=', ''))
        page += 10
        time.sleep(2)
    return urls[:num_results]


if __name__ == "__main__":
    query = "arcgis/rest/services"
    num_results = 1000
    urls = extract_urls(query, num_results)


    df = pd.DataFrame(urls, columns=["URL"])
    df.to_csv("extracted_urls.csv", index=False)
    print(f"Extracted {len(urls)} URLs and saved to extracted_urls.csv")
