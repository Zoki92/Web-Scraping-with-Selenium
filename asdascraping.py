from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


data = []
urlpage = "https://groceries.asda.com/search/bananas"
options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options)

driver.get(urlpage)
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(10)

results = driver.find_elements_by_xpath(
    "//*[@id='listings']/div[2]/div/div/div/div[2]/div[4]/div/div[1]/div/span[2]")


data.append(float(results[0].text[1:5]))
driver.quit()
