from selenium import webdriver

try:
	browser = webdriver.Firefox()
	browser.get('http://www.ubuntu.com/')
	browser.close()
except Exception as e:
	print(e)

print('Task done')