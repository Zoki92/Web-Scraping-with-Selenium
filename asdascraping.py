from selenium import webdriver

import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd

urlpage = "https://groceries.asda.com/search/bananas"
driver = webdriver.Firefox()

driver.get(urlpage)
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(30)

results = driver.find_elements_by_xpath(
    "//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
print('Number of results', len(results))

data = []
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    data.append({"product": product_name, "link": product_link})


driver.quit()
df = pd.DataFrame(data)
df.to_csv('asdaBananas.csv')
