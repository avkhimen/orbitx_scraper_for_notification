from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True

try:
	print('Trying to create the driver')
	driver = webdriver.Firefox(options=options)
except Exception as e:
	print(e)
else:
	try:
		print('Trying to access ubuntu.com')
		driver.get('http://www.ubuntu.com/')
	except Exception as e:
		print(e)
	else:
		time.sleep(10)
		try:
			print('Trying to close the driver')
			driver.close()
		except Exception as e:
			print(e)

print('Task done')