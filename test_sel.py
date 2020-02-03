from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

try:
	driver = webdriver.Firefox(options=options)
	driver.get('http://www.ubuntu.com/')
	driver.close()
except Exception as e:
	print(e)

print('Task done')