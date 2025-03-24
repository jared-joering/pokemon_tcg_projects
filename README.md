## Pokemon TCG Price Analysis

![Pokemon](images/pokemon-logo.png)

#### Project Overview

This is a project of mine, a little professional, but very personal.  I love this hobby, so I set out to find and see if I can extrapolate some insights into card collecting.  At first, as I elaborate in the 'Introduction', I was going to find the best time to purchase cards based upon a years worth of data, but I found a popularity .csv and I thought about that instead.

#### Data Sources

CSVs:

1. tcgplayer-data.csv (gathered by my own webscraper)
2. pokemon-favorites-list.csv

Web Scraper:

1. tcgplayer-scraper.py

#### Installation

Before getting started, you'll need the following:

* Python
* pandas
* Selenium
* numPy
* Beautiful Soup

#### Running the Program
1. As of this submission, Python 3.13.0 was used and Python 3 is required.  Ensure that you have it installed.

2. Clone the repo from GitHub (https://github.com/jared-joering/pokemon_tcg_projects.git).

3. Setup your virtual environment and activate it.

4. To make sure you have all the required packages run:

```
pip install -r requirements.txt
```
5. This was created in Visual Studio Code with Jupyter Notebook.  The main file is "price-history-pokemon-cards.ipynb", as such you will need Jupyter Notebook to run it.

#### Data Dictionary

tcgplayer-data.csv

|Column Index|Column Name|Description|data type|
|---|---|---|---|
|0|'Card'|Pokemon depicted in the card|object|
|1|'Set'|Set containing the card|object|
|2|'Number'|Set number|object|
|3|'Rarity'|Rarity of the card|object|
|4|'Condition'||object|
|5|'Volatility'||object|
|6|'3/18 to 3/24'||object|
|...|'...'|...||
|57|'3/10 to 3/16'||object|

pokemon-favorites-list.csv



final_df

#### Data Analysis Capstone Satisfied Features List

1. Loading Data
        * Read two .csv's ('tcgplayer-data.csv' and 'pokemon-favorites-list.csv')
        * Scraped data with a web scraper (tcgplayer-scraper.py)

2. Clean and operate on the data while combining them
        * Cleaned (removed 'Volatility' and 'Votes') and merged 'tcgplayer-data.csv' and 'pokemon-favorites-list.csv' into 'final_df'.
        * Then calculated two new metrics 'Price-to-Populariy Ratio' and 'Popularity-Adjusted Volatility' (PPR and PAV respectively)
        * Transformed data as well (i.e. splitting and exploding)

3. Visualize / Present your data.
        * Created four charts utilizing seaborn, numpy, and matplotlib.

4. Best practices: Enhance your project to a higher tier that will impress employers and help other programmers understand your project. Choose 2 from this table
        * Utilized a virtual environment, included instructions here.
        * Built a custom Data Dictionary, included here.

5. Interpretation of your data
        * Annotated my code with markdown, wrote clear code comments.  README is well-written.  Everything else is cleaned and functional.

#### Code Louisville: Data Analyst Capstone

TODO: Talk about project
TODO: Talk about methodology
TODO: Talk about installing selenium, beautiful soup, and how to run web scraper
TODO: Data Dictionary
TODO: Talk about future plans