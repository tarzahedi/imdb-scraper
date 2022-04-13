import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint


def main():
    titles = []
    years = []
    time = []
    imdb_ratings = []
    metascores = []
    votes = []
    us_gross = []
    base_url = "https://www.imdb.com"
    url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv" # first page url

    while url:
        print(f'Getting data from {url}')
        headers = {"Accept-Language": "en-US, en;q=0.5"}
        results = requests.get(url, headers=headers)
        soup = BeautifulSoup(results.text, "html.parser")
        movie_div = soup.find_all('div', class_='lister-item mode-advanced')

        for container in movie_div:

            name = container.h3.a.text if container.h3.a else None
            titles.append(name)

            year = _extract_number(container.h3.find(
                'span', class_='lister-item-year').text) if container.h3.find('span', class_='lister-item-year') else None
            years.append(year)

            runtime = _extract_number(container.p.find(
                'span', class_='runtime').text) if container.p.find('span', class_='runtime') else None
            time.append(runtime)

            rating = float(container.strong.text) if container.strong else None
            imdb_ratings.append(rating)

            meta_score = int(container.find('span', class_='metascore').text) if container.find(
                'span', class_='metascore') else None
            metascores.append(meta_score)

            nv = container.find_all('span', attrs={'name': 'nv'})
            gross = None
            vote = None
            for elem in nv:
                inp = elem.text
                if '$' in inp:
                    gross = _extract_float(inp)
                elif '#' not in inp:
                    vote = _extract_number(inp)
            votes.append(vote)
            us_gross.append(gross)
        next_url = soup.find(class_='lister-page-next next-page')
        if next_url:
            url = f"{base_url}{next_url['href']}"
        else:
            url = None
        sleep(randint(1, 5))

    print("Exporting data as movies.csv file...")
    movies = pd.DataFrame({
        'movie': titles,
        'year': years,
        'timeMin': time,
        'imdb': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
        'us_grossMillions': us_gross,
    })

    movies.to_csv('movies.csv', index=False)
    print("Crawling finished successfully")


def _extract_number(inputString):
    """Extracting number in a string
    """
    out = ''
    for char in inputString:
        if char.isdigit():
            out = out + char
    return int(out)


def _extract_float(inputString):
    """Extracting float number in a string
    """
    out = ''
    for char in inputString:
        if char.isdigit() or char == '.':
            out = out + char
    return float(out)


if __name__ == "__main__":
    main()
