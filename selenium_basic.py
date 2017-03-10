from   selenium import webdriver
from   os       import remove
import utils
import time
import sys

_url       = 'https://pypi.python.org/pypi/selenium'
_file_path = 'temp.html'

def save_current_html(_driver):
	file = open(_file_path, 'w')
	file.write(_driver.page_source.encode('utf-8'))
	file.close()

def main():	
	_driver = webdriver.Firefox()
	_driver.get(_url)
	save_current_html(_driver)
	
if __name__ == "__main__":
	main() 	
