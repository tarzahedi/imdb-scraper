# IMDB scraper

Build a web scraper using Python from HTML web pages, and create a DataFrame with pandas.

Scrape data from [IMDb’s Top 1,000 movies](https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv)

There are 50 movies on each page.

## Features

In order to get all the necessary information about each movie, the crawler
GET information from each page and go to the next page until all the data is obtained.

## Final Data

### Sample Data
Extract the following fields for each movie.

* title: name of the movie
* year: the year that movie created
* time: length of the movie in minutes
* imdb_rating: the movie’s IMDb rating 
* metascore: the movie’s Metascore rating
* votes: number of votes that movie achieved
* us_gross: the amount of cost for the movie in million-dollar

Always consider that maybe all the information is not available to scrape. Code should not stop or break for these cases if data is missing.

## How to use

### Requirements

The script uses the following packages:

* jupyterlab
* pandas
* beautifulsoup4
* requests

### setup

install the required packages:

if you want to use virtual env, create it using the following commands:

```shell
python3 -m venv .venv
source ./.venv/bin/activate
```

To install the required packages:

```shell
pip3 install -r requirements.txt
```

## Running the script

You can either use the jupyter notebook or script to get your data. To run the script,
 activate your `virtualenv` and run the following command:

```python
python imdb_scraper.py
```
