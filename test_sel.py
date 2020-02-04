from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import traceback

options = Options()
options.headless = True

try:
	print('Trying to create the driver')
	driver = webdriver.Firefox(options=options)
except Exception as e:
	tb = traceback.format_exc()
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
			print('Task done')
		except Exception as e:
			print(e)
finally:
	print(tb)