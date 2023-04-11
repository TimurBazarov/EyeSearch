import os
import cv2
from bs4 import *
import requests


def folder_create(images):
    try:
        folder_name = input("Enter Folder Name:- ")
        os.mkdir(folder_name)
    except:
        print("Folder Exist with that name!")
        folder_create()
    download_images(images, folder_name)


def download_images(images, folder_name):
    count = 0
    print(f"Total {len(images)} Image Found!")
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass
            try:
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i + 1}.jpg", "wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass
        if count == len(images):
            print("All Images Downloaded!")
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")


def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img', limit=5)
    folder_create(images)


os.chdir('static/models')
filename = input()
a = os.listdir()
m_list = {}
for i in a:
    m_list[i[:i.find('.')]] = cv2.CascadeClassifier(i)
os.chdir('..')
os.chdir('..')
tag_list = []
video_list = ['.mp4', '.avi', '.mkv', '.wmv', '.flv', '.mpeg']
img_list = ['.jpg', '.png', '.bmp', '.gif', '.tif']
if filename[filename.find('.'):] in img_list:
    for x in m_list:
        imaging = cv2.imread(filename)
        imaging_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)
        imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)
        detecting = m_list[x].detectMultiScale(imaging_gray, minSize=(50, 50))
        amountDetecting = len(detecting)
        if amountDetecting != 0:
            if x not in tag_list:
                tag_list.append(x)
            for (a, b, width, height) in detecting:
                cv2.rectangle(imaging_rgb, (a, b),
                              (a + height, b + width),
                              (0, 275, 0), 9)
if filename[filename.find('.'):] in video_list:
    cap = cv2.VideoCapture(filename)
    while True:
        ret, frames = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            for i in m_list:
                car_cascade = m_list[i]
                cars = car_cascade.detectMultiScale(gray, 1.1, 1)
                if not(cars.__class__.__name__ == 'tuple'):
                    if cars.any() and i not in tag_list:
                        tag_list.append(i)
                for (x, y, w, h) in cars:
                    cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # cv2.imshow('video2', frames)
            if cv2.waitKey(33) == 27:
                break
        else:
            break
    cv2.destroyAllWindows()
tags = '%2C'.join(tag_list)
tags.replace('_', '%2C')
print(tags)
url = f'https://unsplash.com/s/photos/{tags}'
res = requests.get(url)
main(url)