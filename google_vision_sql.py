import io
import os
import json
from PIL import Image,ImageDraw,ImageFont
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import mysql.connector
#export GOOGLE_APPLICATION_CREDENTIALS='/home/wenjie/Desktop/601_Mini_project_Database/Mini Project 1/EC601-Pro1-b97efc41859f.json'

def connectdb(ur,pas,database_name):
	db = mysql.connector.connect(user=ur, passwd=pas, database=database_name, use_unicode=True)
	print("Database Connected")
	return db

def operate(db,cmd):
	cursor = db.cursor()
	sql=cmd
	cursor.execute(sql)

def new_user(db,ur,pas):
	cursor = db.cursor()
	sql="""CREATE USER '%s'@'%%' IDENTIFIED BY '%s';"""%(ur,pas)
	cursor.execute(sql)

def create_table(db,table_name):
	cursor=db.cursor()
	cursor.execute("DROP TABLE IF EXISTS "+table_name)
	sql="""CREATE TABLE %s (
	        label CHAR(30) NOT NULL,
	        img_name CHAR(15),
	        USER CHAR(15)
	        )"""%(table_name)
	cursor.execute(sql)



def get_anno(img_path,out_path):
	ur='root'
	pas='wj'
	dab='wj_ec_601'

	db = connectdb(ur,pas,dab)
	cursor=db.cursor()
	table_name="label_to_img"
	create_table(db,table_name)

	client = vision.ImageAnnotatorClient()

	lists=os.listdir(img_path)
	lists.sort()

	images_labels=[]
	for file_name in lists:
		with io.open(img_path+file_name, 'rb') as image_file:
		    content = image_file.read()
		tmp=[]
		tmp.append(file_name)
		image = types.Image(content=content)

		# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations

		print("Dealing with:"+file_name)
		for label in labels:
			tmp.append(label.description)
			#print(label.description)
		
		images_labels.append(tmp)
	#print(images_labels)
	for im in images_labels:
		value=""
		for q in range(len(im)-1):
			if value != "":
				value+=','
			value+="('%s'"%(im[q+1])
			value+=','
			value+="'%s'"%(im[0])
			value+=','
			value+="'%s'"%(ur)
			value+=')'
		#print(value)
		sql = """INSERT INTO %s VALUES %s"""%(table_name,value)
		#print(mysql)
		cursor.execute(sql)
		db.commit()

		img = Image.open(img_path+im[0])
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 30)
		for k in range(len(im)-1):
			draw.text((0, 0+k*30),im[k+1],(15,94,221),font=font)
			img.save(out_path+im[0])

def generate_video(i_path,o_path):
	command="ffmpeg -r 0.5 -i  "+i_path+" "+o_path
	p=os.popen(command)
	p.close()



def main():
	get_anno("./imgs/","./labeled_imgs/")
	generate_video("./labeled_imgs/img%03d.jpg","labeled_video.avi")

if __name__ == '__main__':
	main()