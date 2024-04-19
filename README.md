# StF Takehome

Given a TikTok URL, this repo has the scripts to scrape all the comments on that TikTok reel, and perform sentiment analysis on it. We also added a support to handle scraping of multiple URLs from TikTok. 

## Requirments 

* [geckodriver](https://sourceforge.net/projects/geckodriver.mirror/) - This script uses firefox driver (gecko) to scrape the data as Chrome often has issues with auto-updates
* NLTK - Natural Language Tollkit for sentiment analysis (Available through pip install)
* Beautiful Soup + Selenium for scraping (available through pip install)

## Working 

### Scraper 
* The user can scrape comments from multiple tiktok URLs by dumping all the required data into the `input.json` file.
* Format of input.json: Each entry is a key-value pair where the value is the URL or Tiktok video and the key is the label assigned by the users
* Sample input.json. Here is the sample input data that this code was tested on! 
```
{
    "Ellie1" : "https://www.tiktok.com/@elliegoldenlife/video/7339522920856702251?lang=en",
    "Ellie2" : "https://www.tiktok.com/@elliegoldenlife/video/7358435715090255150?lang=en"
}

```

The scraping script generates one text file for each of the input URLs provided in the `input.json`. Each text file would contain the all the comments on the corresponding TikTok reel. 

### Sentiment Analysis

In order to perform sentiment analysis on the scraped comments, the user can just go to the last cell of the Python notebook provided in the repo and change the name of the file they want to run the sentiment analysis on. 

This generates visualizations and disributions of the classified sentiments for all the comments in the file

## Caution

Tiktok prevents automated scraping so the user. To avoid causing potential problems, the user will have about 10 seconds to complete the "bot check" before the scraping script starts executing. 
