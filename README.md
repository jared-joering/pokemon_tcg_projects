## Pokemon TCG Price Analysis

![Pokemon](images/pokemon-logo.png)

#### About This Project

This project aims to shed a little light on the relationship between popularity and the Pokemon depicted in the card and whether or not that drives prices, increases volatility, and if so: what the impact on those variables actually are.

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

|Column Name|Description|data type|
|---|---|---|
|'Card'|Pokemon depicted in the card|object|
|'Set'|Set containing the card|object|
|'Number'|Set number|object|
|'Rarity'|Rarity of the card|object|
|'Condition'|The condition of the card|object|
|'Volatility'|A metric of price fluctuations|object|
|'3/18 to 3/24'|Price during the week of March 3/18 to 3/24|float64|
|...|...|...|
|'3/10 to 3/16'|Price during the week of March 3/10 to 3/16|float64|

> Note: Columns from '3/18 to 3/24' on to '3/10 to 3/16' represent weekly price ranges for the full year.

pokemon-favorites-list.csv

|Column Name|Description|data type|
|---|---|---|
|Pokemon|Name of the Pokemon|object|
|Number of votes|How many votes the Pokemon got|Int64|
|Rank|The respective ranking for each Pokemon|Int64|

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