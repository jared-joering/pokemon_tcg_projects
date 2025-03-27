![Pokemon](images/pokemon-logo.png)

#### About This Project

At first, this project was created to see when the best time was to buy cards.  Now, that is still the case and I fully intend on fleshing this project out in the future.  During my search for useable APIS, I did happen upon a popularity chart and thus this iteration was born.  With that said, this project aims to shed a faint light on the relationship between popularity and the Pokemon depicted in the card and whether or not that drives prices, increases volatility, and if so: what the impact on those variables actually are and whether or not a deeper, more thorough search is warranted. <img src = "images/pikachu-magnifying-glass.png" alt = "Pikachu from Detective Pikachu" align = "right" style = "length: 25%; width: 25%;">

#### Information and Troubleshooting

* If the price-history-pokemon-cards.ipynb errors on the first Run All, be patient and click it again.

* As far as the tcgplayer-scraper.py is concerned, that's a bit more fickle but only insofar as the data entry is concerned.  For that, you should monitor your tcgplayer-data.csv.  There may be some values missed.  If that happens, delete the row, and then re-add it.  This usually happens with older cards.  

* The scraper, as it currently stands (3/27) does not check for duplicate entries into the database.  Be careful!

* If there are no values in the '1Y' chart for the card of your choice, the scraper **will** return an error.  

#### Data Sources

CSVs:

1. tcgplayer-data.csv (gathered by my own webscraper)
2. pokemon-favorites-list.csv

Web Scraper:

1. tcgplayer-scraper.py

#### Installation

Before getting started, you'll need the following for the .ipynb to be read:

* Python
* pandas
* numPy

And these for the tcgplayer-scraper.py:

* Selenium
* Beautiful Soup
* webdriver_manager

All of these can be found at step 4.

#### Running the Notebook
1. As of this submission, Python 3.13.0 was used and Python 3 is required.  Ensure that you have it installed.

2. Clone the repo from GitHub (https://github.com/jared-joering/pokemon_tcg_projects.git).

3. Setup your virtual environment and activate it.

4. To make sure you have all the required packages run:

```
pip install -r requirements.txt
```

> *Note: Both this project and the web scraper were created and tested in Visual Studio Code with Jupyter Notebook on two machines.  One was a laptop and another a desktop, both Windows.*

#### Running the Web Scraper

You'll need [FireFox](https://www.mozilla.org/en-US/firefox/new/).  That's it!

### Using the Web Scraper

To run the web scraper, you'll just need to run the script and then find the full-URL of the card you wish to enter (i.e. 'https://www.tcgplayer.com/product/201352/pokemon-sm-cosmic-eclipse-pikachu-secret?Condition=Near+Mint&Language=English&page=1').  This card has been purposefully left out of the database.  Give it a try!

#### Custom Data Dictionary

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

> *Note: Columns from '3/18 to 3/24' on to '3/10 to 3/16' represent weekly price ranges for the full year.*

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