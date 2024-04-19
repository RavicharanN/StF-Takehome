from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import os
import json

# Set up Firefox driver
firefox_options = Options()
firefox_path = "/Users/ravicharan/Downloads/geckodriver"  # Replace with the path to your geckodriver executable
driver = webdriver.Firefox(options=firefox_options)

# Scrapes comments when URL is given as the input
def scrape_comments(video_url):
    driver.get(video_url)

    # This time is to manually add a sleep to verfiy human checks
    time.sleep(10)

    # This block loads more all the comments first ...
    # ... by scrolling all the way to the bottom
    last_height = driver.execute_script("return document.body.scrollHeight")
    cnt = 0 # Optiinal - this is just a regularizer to precent too much scrolling 
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new comments to load
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        # ----- optional blockL: break if scrolled over 10 times ------
        cnt += 1
        if (cnt > 4):
            break

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    comment_elements = soup.find_all('p', {'data-e2e': 'comment-level-1'})

    comments  = []
    for comment_element in comment_elements:
        comment_text = comment_element.text.strip()
        comments.append(comment_text)

    return comments

# Dump comments to file
def dump_comments_to_file(comments, filename):
    print("Writing to :", filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as file:
        for comment in comments:
            file.write(comment + '\n')

# This block is added to support multiple labels and video URLs at the same time 
url_labels_dict = {}

# Open the JSON file and load its contents into our dictionary
with open('input.json', 'r') as file:
    url_labels_dict = json.load(file)

for key in url_labels_dict.keys():
    video_url = url_labels_dict[key]
    comments = scrape_comments(video_url)
    filename = "scraped_comments/" + str(key) + '.txt'
    dump_comments_to_file(comments, filename)

driver.quit()
