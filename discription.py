import bs4
import re
import requests
from urllib.request import urlopen as uReq
import urllib.request as req
from bs4 import BeautifulSoup as soup
import random

def descriptions(name):
	name = name.replace(' ', '-')
	url = 'https://www.thetvdb.com/series/'+name
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll("div",{"class":"change_translation_text"})
	if len(data) !=0:
		value = (data[0].p.string).replace("'",",")
	else:
		value = 'Sorry!! for the Inconvinence. We Dont have enough words to Describe this series.'
		
	return(value)
# Old method
# def image_request(name):
# 	name = name.replace(' ', '-')
# 	url = 'https://www.thetvdb.com/series/'+name
# 	uClient = uReq(url)
# 	page_html = uClient.read()
# 	uClient.close()
# 	page_soup = soup(page_html, "html.parser")
# 	data = page_soup.findAll("img",{"class":"media-object img-responsive"})
# 	if len(data) != 0 :
# 		for img in data:
# 			if 'graphical' in img.get('src'):
# 				return (img.get('src'))
# 	else:
# 		return('static/blue.jpg')

# New Method
def image_request(name):
	name = name.replace(' ', '-')
	url = 'https://www.thetvdb.com/series/'+name+'/artwork/banners'
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll("img",{"class":"media-object img-responsive"})
	if len(data) != 0 :
		li = []
		for img in data:
			li.append(img.get('src'))
		# ','.join(li)
		if len(li) >= 10:
			return (','.join(li[:10]))
		else:
			return (','.join(li))
	else:
		return('static/blue.jpg')


def rating_request(name):
	name = name.replace(' ', '-')
	url = 'https://www.thetvdb.com/series/'+name
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll("li",{"class":"list-group-item clearfix"})
	if len(data) != 0 :
		new_link = data[8].a.get('href')
		new_uClient = uReq(new_link)
		new_page_html = new_uClient.read()
		new_uClient.close()
		new_page_soup = soup(new_page_html, "html.parser")
		new_data =new_page_soup.findAll("div",{"class":"ratingValue"})
		if len(new_data) != 0:
			return new_data[0].strong.get('title').split(' ')[0]
		else:
			return('not rated')
	else:
		return('not rated')
# Old Method
# def image_request_back_banner(name):
# 	name = name.replace(' ', '-')
# 	url = 'https://www.thetvdb.com/series/'+name
# 	uClient = uReq(url)
# 	page_html = uClient.read()
# 	uClient.close()
# 	page_soup = soup(page_html, "html.parser")
# 	data = page_soup.findAll("img",{"class":"img-responsive full_width_image"})
# 	if len(data) != 0:
# 		for img in data:
# 			return (img.get('src'))
# 	else:
# 		return('static/back_img.jpg')
# New Method
def image_request_back_banner(name):
	name = name.replace(' ', '-')
	url = 'https://www.thetvdb.com/series/'+name+'/artwork/fanart'
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll("img",{"class":"media-object img-responsive"})
	if len(data) != 0:
		for img in data:
			li = []
			for img in data:
				li.append(img.get('src'))
		if len(li) >= 10:
			return (','.join(li[0:10]))
		else:
			return (','.join(li))
	else:
		return('static/back_img.jpg')

# print(image_request_back_banner('game of thrones'))

# print(image_request('game of thrones')[random.randint(0,9)])