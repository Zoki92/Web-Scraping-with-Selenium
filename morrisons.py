from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


data = []
url = "https://www.mysupermarket.co.uk/"
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)
driver.find_element_by_xpath(
    "//*[@id='homePage']/div[1]/div[2]/div/ul[2]/li[3]")
