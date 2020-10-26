# Import Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time

#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=False)
# MARS NEWS URL FOR TITLE AND PARAGRAPH
#news_url = 'http://mars.nasa.gov/news'
#browser.visit(news_url)
#html = browser.html
#news_soup = bs(html, 'html.parser')
#news = news_soup.find_all('div', class_='bottom_gradient')[0].text.strip()
#print(news)

# MARS LATEST NEWS - div class article teaser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

para_url = 'https://mars.nasa.gov/news/'
browser.visit(para_url)
# HTML Object
html = browser.html
soup = bs(html, 'html.parser')

paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
print(paragraph)


# FEATURED IMAGE URL
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=False)
#image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#browser.visit(image_url)
# HTML Object
#featured_html = browser.html
#featured_soup = bs(featured_html, 'html.parser')
#images = featured_soup.find('footer')
#link = images.find('a')['data-fancybox-href']
#featured_image_url = image_url + link

