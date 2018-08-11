import socket
import time
REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
	try:
		s = socket.create_connection((socket.gethostbyname(hostname), 80), 2)
		return True
	except:
		pass
	return False

while is_connected(REMOTE_SERVER) is False:
	print('We will be back after a while')
	time.sleep(10)