from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit NASA Mars News
    url = "http://mars.nasa.gov/news"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get Mars Latest News and Description
    title = soup.find_all('div', class_='content_title')[0].text
    paragraph = soup.find_all('div', class_='rollover_description_inner')[0].text


    # Featured Image
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    
    # HTML Object
    featured_html = browser.html
    featured_soup = bs(featured_html, 'html.parser')
    images = featured_soup.find('footer')
    link = images.find('a')['data-fancybox-href']
    featured_image = image_url + link

    # Mars Facts
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_facts_url = 'https://space-facts.com/mars/'
    mars_facts = pd.read_html(mars_facts_url)
    mars_df = mars_facts[0]
    mars_df.columns = ["Mars", "Mars Facts"]
    mars_facts_html = mars_df.to_html()
    mars_facts_html.replace('\n', '')

    # HEMISPHERE IMAGE LINKS
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    cerberus_link = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(cerberus_link)
    cerberus_html = browser.html
    cerberus_soup = bs(cerberus_html, 'html.parser')
    cerberus = cerberus_soup.find('li').a['href']
    #  print(cerberus)

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



    # Store data in a dictionary
    mars_data = {
        "title": title,
        "paragraph": paragraph,
        "featured_image": featured_image,
        "facts": str(mars_facts_html),
        "cerberus": cerberus,
        "schiaparelli": schiaparelli,
        "syrtis_major": syrtis_major,
        "valles_marineris": valles_marineris
     }

    print(mars_data)
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data













   



