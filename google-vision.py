import io
import os
import json
from PIL import Image,ImageDraw,ImageFont
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


#export GOOGLE_APPLICATION_CREDENTIALS="/home/wenjie/Desktop/Mini Project 1/[file_name].json"
def get_anno(img_path,out_path):
	# Instantiates a client
	client = vision.ImageAnnotatorClient()

	# The name of the image file to annotate


	lists=os.listdir(img_path)
	lists.sort()



	"""
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    'imgs/img001.jpg')
	"""

	images_labels=[]
	# Loads the image into memory


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

	for im in images_labels:
		img = Image.open(img_path+im[0])
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 25)
		for k in range(len(im)-1):
			draw.text((0, 0+k*25),im[k+1],(255,0,0),font=font)
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