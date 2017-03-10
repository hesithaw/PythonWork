from   selenium import webdriver
from selenium.webdriver.common.keys import Keys
from   os       import remove
import utils
import time
import sys

_url       = 'http://www.google.com'
_file_path = 'temp.html'

def save_current_html(_driver):
	file = open(_file_path, 'w')
	file.write(_driver.page_source.encode('utf-8'))
	file.close()

def main():	
	_driver = webdriver.Firefox()
	_driver.get(_url)
	save_current_html(_driver)
	time.sleep(5)
	elem = _driver.find_element_by_name('q')  # Find the search box
	elem.send_keys('seleniumhq' + Keys.RETURN)
	
if __name__ == "__main__":
	main() 	
