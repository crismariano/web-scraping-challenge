# Import Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time


# MARS NEWS URL FOR TITLE AND PARAGRAPH
url = 'http://mars.nasa.gov/news'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
title = soup.find_all('div', class_='content_title')[0].text
paragraph = soup.find_all('div', class_='rollover_description_inner')[0].text

# Print statements checked during the scrape build to make sure that data was being pulled.
#print(title)
#print(paragraph)

# FEATURED IMAGE URL
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)
# HTML Object
featured_html = browser.html
featured_soup = bs(featured_html, 'html.parser')
images = featured_soup.find('footer')
link = images.find('a')['data-fancybox-href']
featured_image_url = image_url + link

# Print statement checked during the scrape build to make sure that data was being pulled.
# print(featured_image_url)

# HEMISPHERE TITLES
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
titles = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(titles)
titles_html = browser.html
titles_soup = bs(titles_html, 'html.parser')

mars_hemi_titles = titles_soup.find_all('h3')
for x in mars_hemi_titles:
    print(x.text)

# HEMISPHERE IMAGE LINKS
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
cerberus_link = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
browser.visit(cerberus_link)
cerberus_html = browser.html
cerberus_soup = bs(cerberus_html, 'html.parser')
cerberus = cerberus_soup.find('li').a['href']
#print(cerberus)

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
schiaparelli_link = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
browser.visit(schiaparelli_link)
schiaparelli_html = browser.html
schiaparelli_soup = bs(schiaparelli_html, 'html.parser')
schiaparelli = schiaparelli_soup.find('li').a['href']
#print(schiaparelli)

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
syrtis_major_link = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
browser.visit(syrtis_major_link)
syrtis_major_html = browser.html
syrtis_major_soup = bs(syrtis_major_html, 'html.parser')
syrtis_major = syrtis_major_soup.find('li').a['href']
#print(syrtis_major)

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
valles_marineris_link = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
browser.visit(valles_marineris_link)
valles_marineris_html = browser.html
valles_marineris_soup = bs(valles_marineris_html, 'html.parser')
valles_marineris = valles_marineris_soup.find('li').a['href']
#print(valles_marineris)
    
# MARS FACTS
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
mars_facts_url = 'https://space-facts.com/mars/'
mars_facts = pd.read_html(mars_facts_url)
mars_df = mars_facts[2]
mars_df.columns = ["Mars", "Mars Facts"]
mars_facts_html = mars_df.to_html()
mars_facts_html.replace('\n', '')




# Create a dictionary for the Mars title, paragraph, and URL links

mars_scraped_data =  {
    "title": title,
    "paragraph": paragraph,
    "featured_image": featured_image_url,
    "cerberus": cerberus,
    "schiaparelli": schiaparelli,
    "syrtis_major": syrtis_major,
    "valles_marineris": valles_marineris,
    "facts": mars_facts_html
    }

print(mars_scraped_data)
