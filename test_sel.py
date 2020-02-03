from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.ubuntu.com/')
browser.close()

print('Task done')