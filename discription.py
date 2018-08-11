import bs4
import re
import requests
from urllib.request import urlopen as uReq
import urllib.request as req
from bs4 import BeautifulSoup as soup

def descriptions(name):
	name = name.replace(' ', '-')
	url = 'https://www.thetvdb.com/series/'+name
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll("div",{"class":"change_translation_text"})
	value = (data[0].p.string).replace("'",",")
	return(value)

def image_request(name):
	name = name.replace(' ', '-')
	url = 'https://www.thetvdb.com/series/'+name
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll("div",{"class":"series_header large"})
	# value = (data[0].p.string).replace("'",",")
	return(data[0].img.get('src'))

print(image_request('stranger things'))

	

