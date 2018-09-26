from flask import Flask,render_template,request,make_response,jsonify
import mysql.connector
import urllib.request
from discription import descriptions , image_request, rating_request, image_request_back_banner
import urllib.parse, json
import random
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="show")
# mydb = mysql.connector.connect(host="192.168.1.9",user="pmauser",passwd="amitpi",database="show")
mycursor = mydb.cursor()


app = Flask(__name__)
@app.route('/')
def index ():
	sql = "SELECT `background img` FROM `description`"
	mycursor.execute(sql)
	auto= mycursor.fetchall()
	front_image = []
	for pic in auto:
		for each_pic in pic[0].split(','):
			front_image.append(each_pic)
	image = front_image[random.randint(0,len(front_image))]
	return render_template('index.html',image = image)

@app.route('/data', methods = ['POST','GET'])
def data():
	if request.method == 'POST':
		season_name = request.form['season_name']
		season_name_for_discp = season_name
		season_name = season_name.replace(' ', '%20')
		first_letter = season_name[0]
		image_request_back = ""
		image_back = ""
		season_number = request.form['season_number']
		if season_number[0] == 'S' or season_number[0] == 's':
			season_number = season_number[1:]
		if len(season_number) == 1:
			season_number = "0"+season_number

		episode_number = request.form['episode_number']
		if episode_number[0] == 'E' or episode_number[0] == 'e':
			episode_number = episode_number[1:]
		if len(episode_number) == 1:
			episode_number = "0"+episode_number
		sql = "SELECT link,size FROM `"+first_letter+"` WHERE link LIKE '%"+season_name+"%'"
		mycursor.execute(sql)
		a = mycursor.fetchall()
		temp = []
		for i in a:
			if ("S"+season_number) in i[0]:
				if ("E"+episode_number) in i[0]:
					templist = []
					templist.append(i[0])
					size = i[1]
					if float(size)>1024:
						size = str(round(int(size)/1024,2)) + " GB"
					else:
						size = str(round(float(size),2)) + " MB"
					templist.append(size)
					temp.append(templist)
					new_sql = "SELECT `description`, `image_link`, `rating`,`background img` FROM `description` WHERE `season_name` LIKE '"+season_name+"';"
					mycursor.execute(new_sql)
					d = mycursor.fetchall()
					autocomplete = "SELECT `season_name` FROM `season_name` WHERE `season_name` LIKE '%"+season_name_for_discp+"%'"
					mycursor.execute(autocomplete)
					auto = mycursor.fetchall()
					if len(auto) == 0:
						autocomplete1 = "INSERT INTO `season_name`(`season_name`) VALUES ('"+season_name_for_discp+"');"
						mycursor.execute(autocomplete1)
						mydb.commit()
					if len(d) == 0:
						discp = descriptions(season_name_for_discp)
						img_src = image_request(season_name_for_discp)
						rating_of_show = rating_request(season_name_for_discp)
						image_request_back = image_request_back_banner(season_name_for_discp)
						sql = "INSERT INTO `description`(`season_name`, `description`, `image_link`, `rating`,`background img`) VALUES ('"+season_name+"','"+discp+"','"+img_src+"','"+rating_of_show+"','"+image_request_back+"');"
						mycursor.execute(sql)
						mydb.commit()
					else:
						discp = d[0][0]
						img_src= d[0][1]
						rating_of_show = d[0][2]
						image_back = d[0][3]
						discp = str(discp).replace("\n","").replace("(' ","").replace("',)","")

		if len(temp) != 0:
			li = img_src.split(',')
			img_src = li[random.randint(0,(len(li)-1))]
			nli = image_back.split(',')
			image_back = nli[random.randint(0,(len(li)-1))]

			return render_template('data.html',rating_of_show = rating_of_show ,image_back = image_back, link = temp, discp = discp, img_src = img_src, season_name=season_name,season_number=season_number,episode_number=episode_number)
		else:
			season_name = season_name.replace('%20','_')
			print(season_name)
			print(season_number)
			print(episode_number)
			sql = "SELECT link,size FROM `"+first_letter+"` WHERE link LIKE '%"+season_name+"%'"
			mycursor.execute(sql)
			a = mycursor.fetchall()
			print(a)

	return render_template('index.html')

@app.route('/vid', methods = ['POST','GET'])
def vid():
	print(temp)
	return render_template('vid.html' )

@app.route('/find', methods = ['POST','GET'])

def find():

		return render_template('find.html')


@app.route('/searched', methods = ['POST','GET'])
def searched():
		series_name = request.form['series_name']
		print(series_name[0])

		sql = 'SELECT `link` FROM `'+series_name[0]+'` WHERE `link` LIKE "%'+series_name+'%"'
		mycursor.execute(sql)
		search = mycursor.fetchall()

		for li in search:
			lin = li[0]

		return render_template('searched.html',series_name = series_name, search = search )


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
