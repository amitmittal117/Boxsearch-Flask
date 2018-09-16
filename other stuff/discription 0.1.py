import bs4
import re
import requests
from urllib.request import urlopen as uReq
import urllib.request as req
from bs4 import BeautifulSoup as soup

def disc(name):
	imdb = 'https://www.imdb.com'
	url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q='+name.replace(" ", "%20")+'&s=all'
	def retrive(url):
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		page_soup = soup(page_html, "html.parser")
		return page_soup

	data = retrive(imdb+ retrive(url).findAll("td",{"class":"result_text"})[0].a.get('href')).findAll("div",{"class":"summary_text"})

	return (data[0].string)
