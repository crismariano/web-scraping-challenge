# Import Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    
    # Visit Mars url
    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    time.sleep(1)

    #Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Mars Data Title and Paragraphe description
    title = soup.find_all('div', class_='content_title')[0].text.strip()
    paragraph = soup.find_all('div', class_='rollover_description_inner')[0].text.strip()

    # Store Data in a Dictionary
    mars_data = {
        "title": title,
        "paragraph": paragraph,
    }

    print(mars_data)
    # Close the browser after scraping
    browser.quit

    # Return Results
    return mars_data