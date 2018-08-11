from flask import Flask,render_template,request,make_response
import mysql.connector
import urllib.request 
from discription import descriptions , image_request
import urllib.parse, json
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="show")
mycursor = mydb.cursor()


app = Flask(__name__)
@app.route('/')
def index ():
	sql = "SELECT `season_name` FROM `season_name`"
	mycursor.execute(sql)
	auto= mycursor.fetchall()
	autodict = {}
	for i in auto:
		autodict[i[0]] = 'null'

	return render_template('index.html' ,autodict = autodict)

@app.route('/data', methods = ['POST','GET'])
def data():
	if request.method == 'POST':
		season_name = request.form['season_name']
		season_name_for_discp = season_name
		season_name = season_name.replace(' ', '%20')
		first_letter = season_name[0]
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
		# sql = "SELECT link FROM demo_mark_3 WHERE season_name = '"+season_name+"' AND season_number = '"+ season_number +"' AND episode_number = '"+ episode_number +"'"
		# sql = "SELECT link FROM demo_mark_3 WHERE link LIKE '%"+season_name+"%' AND link LIKE '%"+season_number+"%' AND link LIKE '%"+episode_number+"%'"
		sql = "SELECT link,size FROM "+first_letter+" WHERE link LIKE '%"+season_name+"%'"
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
					new_sql = "SELECT `description`, `image_link` FROM `description` WHERE `season_name` LIKE '"+season_name+"';"
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
						sql = "INSERT INTO `description`(`season_name`, `description`, `image_link`) VALUES ('"+season_name+"','"+discp+"','"+img_src+"');"

						mycursor.execute(sql)
						mydb.commit()
					else:
						discp = d[0][0]
						# print(d)
						img_src= d[0][1]
						discp = str(discp).replace("\n","").replace("(' ","").replace("',)","")
		if len(temp) != 0:
			return render_template('data.html', link = temp,discp = discp,img_src = img_src, season_name=season_name,season_number=season_number,episode_number=episode_number)
	
	return render_template('index.html')

@app.route('/vid', methods = ['POST','GET'])
def vid():
	print(temp)
	return render_template('vid.html' )


if __name__ == "__main__":
	app.run(debug=True)
