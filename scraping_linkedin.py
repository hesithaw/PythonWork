"""-----------------------------------------------------------
    Python Selenium Script for LinkedIn Scrape
   ----------------------------------------------------------"""

#FILE IMPORTS
from   selenium import webdriver
from   os       import remove
from selenium.webdriver.common.keys import Keys
import utils
import time
import sys 
import argparse  
from bs4 import BeautifulSoup, SoupStrainer
import requests

#SCRAPER GLOBALS
_url       = 'https://www.linkedin.com'
_file_path = 'temp.html'
_out_file_path = 'out.txt'

#INIT THE DRIVER
_driver = webdriver.Firefox()

#LOGIN AND ADVANCED SEARCH FOR CL ARGS
def login_and_search(args):
	_driver.get(_url)
	user     = _driver.find_element_by_xpath('//*[@id="login-email"]')
	password = _driver.find_element_by_xpath('//*[@id="login-password"]')
	
	user.send_keys(args.user)
	password.send_keys(args.password)
	_driver.find_element_by_xpath('//*[@id="login-submit"]').click()

	time.sleep(20)

	_driver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button').click()
	time.sleep(5)
	search = _driver.find_element_by_xpath('//*[@class="ember-text-field ember-view"]')
	search.send_keys(args.keyword + Keys.RETURN)
	
	time.sleep(5)
	_driver.execute_script("window.scrollTo(0, 10000);")
	time.sleep(5)
	save_current_html()

def save_current_html():
    file = open(_file_path, 'w')
    file.write(_driver.page_source.encode('utf-8'))
    file.close()
			
#Page parsing functions
def parse_page(file_path, out_file_path):
	file = open(file_path, 'r')
	parser = BeautifulSoup(file, "html.parser", parse_only=SoupStrainer('div', {"class" : "search-result__info pt3 pb4 ph0"}))
	collection = parser.findAll('a', { "class" :'search-result__result-link ember-view'})
	for items in collection:
		write_results(_url + items.get('href') + '\n', out_file_path)
	write_results('----------------------------------------------\n', out_file_path)
	file.close()
	
def write_results(results, out_file_path):
	file = open(out_file_path, 'a')
	file.write(results)
	file.close()
	
def teardown():
    try:
        remove(_file_path)
    except:
        print('Temp file does not exist')

def init_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u",        dest="user", 			help=" User Name  ")
	parser.add_argument("-p",        dest="password",             help=" Password ")
	parser.add_argument("-key",        dest="keyword",            	help=" Key Words ")    
	return parser
	
def parse_arguments(parser):
    args = parser.parse_args()
    args.url = _url 	
    return args   	

def main():
	parser = init_arguments()
	args = parse_arguments(parser)
	login_and_search(args)
	parse_page(_file_path, _out_file_path)
	teardown()
	_driver.quit()

if __name__ == "__main__":
	main()  	
