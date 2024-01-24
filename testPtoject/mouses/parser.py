import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from lxml import html


# catalog-product__name ui-link ui-link_black
# url = 'https://www.citilink.ru/catalog/holodilniki/'


def parseDns():
	# url = 'https://www.citilink.ru/catalog/holodilniki/'
	# response = requests.get(url).text
	# soup = BeautifulSoup(response,'lxml')
	# print(soup)
	# r = requests.get(url)
	# with open('test.html', 'w') as output_file:
 #  		output_file.write(r.text)

	page_num = 1
	url = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?p={}&i=1&mode=list&brand=brand-apple'.format(page_num)

	driver = webdriver.Firefox()
	driver.get(url)

	content = driver.page_source
	tree = html.fromstring(content)

	print(tree.xpath('//span[@class=" item edge"]')[0].attrib)

	last_page = tree.xpath('//span[@class=" item edge"]')[0].attrib.get('data-page-number')

	print(last_page)
	
parseDns()