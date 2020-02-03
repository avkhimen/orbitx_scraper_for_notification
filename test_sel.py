from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True

try:
	driver = webdriver.Firefox(options=options)
	driver.get('http://www.ubuntu.com/')
	time.sleep(10)
	driver.close()
except Exception as e:
	print(e)

print('Task done')