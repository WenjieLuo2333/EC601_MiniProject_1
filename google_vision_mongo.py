import io
import os
import json
from PIL import Image, ImageDraw, ImageFont
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import pymongo
# export
# GOOGLE_APPLICATION_CREDENTIALS='/home/wenjie/Desktop/601_Mini_project_Database/Mini
# Project 1/EC601-Pro1-b97efc41859f.json'


def connectdb():
    db = pymongo.MongoClient()
    return db


def get_anno(account, img_path, out_path):

    db = connectdb()
    tdb = db.wj_601
    table = tdb.account_info
    table.drop()
    table = tdb.account_info
    client = vision.ImageAnnotatorClient()

    lists = sorted(os.listdir(img_path))

    images_labels = []
    for file_name in lists:
        with io.open(img_path + file_name, 'rb') as image_file:
            content = image_file.read()
        tmp = []
        tmp.append(file_name)
        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print("Dealing with:" + file_name)
        for label in labels:
            tmp.append(label.description)
            # print(label.description)

        images_labels.append(tmp)
    # print(len(images_labels))
    insert_target = [{'Account': account, 'Img_Name': i[0],
                      'Labels':i[1:-1]} for i in images_labels]
    # print(len(insert_target))
    table.insert_many(insert_target)

    for im in images_labels:

        img = Image.open(img_path + im[0])
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/freefont/FreeMono.ttf", 30)
        for k in range(len(im) - 1):
            draw.text((0, 0 + k * 30), im[k + 1], (15, 94, 221), font=font)
            img.save(out_path + im[0])


def generate_video(i_path, o_path):
    command = "ffmpeg -r 0.5 -i  " + i_path + " " + o_path
    p = os.popen(command)
    p.close()


def main():
    get_anno("@NBA", "./imgs/", "./labeled_imgs/")
    # generate_video("./labeled_imgs/img%03d.jpg","labeled_video.avi")


if __name__ == '__main__':
    main()
