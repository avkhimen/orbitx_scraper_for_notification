
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

try:
    driver.get("https://www.orbitxch.com/customer")
    time.sleep(10)
except Exception as e:
    print("Couldn't load site")
try:
    xpath_path = "/html/body/div[1]/div[1]/div[2]/div[3]/div/div[1]/div/ul/li[3]/a"
    soccer_button = driver.find_element_by_xpath(xpath_path)
    soccer_button.click()
    time.sleep(10)
except Exception as e:
    print("Couldn't find 'soccer' button")
try:
    xpath_path = "/html/body/div[1]/div[1]/div[3]/div/div/div/div"\
    "[2]/div[3]/div/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div/div/div[3]/a[1]"
    next_button = driver.find_element_by_xpath(xpath_path)
    next_button.click()
    time.sleep(10)
except Exception as e:
    print("Couldn't find 'next' button")
print("Page 2")
try:
    i = 1
    while i < 21:
         xpath_path = "/html/body/div[1]/div[1]/div[3]/div/div/div/div"\
         "[2]/div[3]/div/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/div"\
         "/div[2]/div[2]/div/div/div[" + str(i) + "]/table/tbody/tr/td[2]/div"
         result = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')
         print(result)
         i += 1
except Exception as e:
    print(e)
print("Page 3")
try:
    xpath_path = "/html/body/div[1]/div[1]/div[3]/div/div/div/div"\
    "[2]/div[3]/div/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div/div/div[3]/a[1]"
    next_button = driver.find_element_by_xpath(xpath_path)
    next_button.click()
    time.sleep(10)
except Exception as e:
    print("Couldn't find 'next' button")
try:
    i = 1
    while i < 21:
         xpath_path = "/html/body/div[1]/div[1]/div[3]/div/div/div/div"\
         "[2]/div[3]/div/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/div"\
         "/div[2]/div[2]/div/div/div[" + str(i) + "]/table/tbody/tr/td[2]/div"
         result = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')
         print(result)
         i += 1
except Exception as e:
    print(e)
print("Page 4")
try:
    xpath_path = "/html/body/div[1]/div[1]/div[3]/div/div/div/div"\
    "[2]/div[3]/div/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div/div/div[3]/a[1]"
    next_button = driver.find_element_by_xpath(xpath_path)
    next_button.click()
    time.sleep(10)
except Exception as e:
    print("Couldn't find 'next' button")
try:
    i = 1
    while i < 21:
         xpath_path = "/html/body/div[1]/div[1]/div[3]/div/div/div/div"\
         "[2]/div[3]/div/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/div"\
         "/div[2]/div[2]/div/div/div[" + str(i) + "]/table/tbody/tr/td[2]/div"
         result = driver.find_element_by_xpath(xpath_path).get_attribute('innerHTML')
         print(result)
         i += 1
except Exception as e:
    print(e)

driver.close()