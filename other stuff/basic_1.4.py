import bs4
import requests
from urllib.request import urlopen as uReq
import urllib.request as req
from bs4 import BeautifulSoup as soup
import mysql.connector
import socket
import time
REMOTE_SERVER = "www.google.com"

#---------------Url to Use----------------
# any_url = "http://dl.upload8.net/Serial/Gotham/"
any_url = "http://dl.sitemovie.ir/serial/TEEN%20WOLF/s1/"
# any_url = "http://dl.upload8.net/Serial/Agents.of.S.H.I.E.L.D/"
# any_url = "http://fromv.ir/vip/Series/Ongoing/Arrow/"
#------------Database in Action------------
host = "localhost"
user = "root"
passwd = ""
database = "show"
#-------------------------------------------

mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database)
mycursor = mydb.cursor()

def is_connected(hostname):
	try:
		s = socket.create_connection((socket.gethostbyname(hostname), 80), 2)
		return True
	except:
		pass
	return False


def fun(any_url):
	while is_connected(REMOTE_SERVER) is False:
		print('We will be back after a while')
		time.sleep(10)
	url = any_url
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll("a")

	for link in data:
		if link.get("href")[-1] == '/' and  link.get("href")[0] != '.':
			fun(url+link.get("href"))  
		elif link.get("href")[0] != '?' and link.get("href")[0] != '.':
			size = str(round((req.urlopen(any_url + link.get("href")).length)/(1024*1024)))
			# print(link.get("href"))
			# sql = 'INSERT INTO `'+link.get("href")[0]+'`(link,size) VALUES("'+any_url + link.get("href")+'")'
			sql = 'INSERT INTO `'+link.get("href")[0]+'`(`link`, `size`) VALUES ("'+any_url + link.get("href")+'","'+size+'")'
			print(sql)
			mycursor.execute(sql)
			mydb.commit()

			print(any_url + link.get("href"))

fun(any_url)
