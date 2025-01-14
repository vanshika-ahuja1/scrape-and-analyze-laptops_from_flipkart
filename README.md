# Flipkart Laptop Scraping and EDA
This project involves web scrapping of laptop data from Flipkart and performing EDA on collected data.The aim is to gather various information on various aspects of laptops including:
* Brand name
* Prices
* Rating
* Gaming
* RAM
and many more.

## How to use the project
to use this project you'll need to have python and its libraries like BeautifulSoup,Selenium,Pandas,Numpy,matplotlib,Seaborn.
for scrapping the data firstly run main1.py then collect.py.this will fetch the data from flipkart and save the data to _laptop_data.csv
After scrapping thd data you can use Laptop_data_analysis.ipynb to perform EDA.


BeautifulSoup handles parsing the HTML content of the webpages, while Selenium helps in dealing with dynamic content that might require additional interaction.After collecting the data, the project performs EDA . This may involve:
* Data cleaning
* Data Visualisation
* Statstical Analysis

By analyzing the scraped data, we can gain valuable insights such as:
* Which product has the highest rating?
* How many products have a rating of 4.5 or higher?
* What is the average number of RAM (in GB) across all products?
