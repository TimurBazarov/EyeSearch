import cv2
import os
from matplotlib import pyplot as pltd
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
imaging = cv2.imread("test3.jpg")
imaging_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)
imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)
detecting = m_list['cars'].detectMultiScale(imaging_gray,
                                    minSize =(30, 30))
amountDetecting = len(detecting)
if amountDetecting != 0:
    for(a, b, width, height) in detecting:
        cv2.rectangle(imaging_rgb,(a, b),
                        (a + height, b + width),
                        (0, 275, 0), 9)
detecting = m_list['speed_road_sign'].detectMultiScale(imaging_gray,
                                    minSize =(30, 30))
amountDetecting = len(detecting)
if amountDetecting != 0:
    for(a, b, width, height) in detecting:
        cv2.rectangle(imaging_rgb,(a, b),
                        (a + height, b + width),
                        (0, 275, 0), 9)
detecting = m_list['stop_road_sign'].detectMultiScale(imaging_gray,
                                    minSize =(30, 30))
amountDetecting = len(detecting)
if amountDetecting != 0:
    for(a, b, width, height) in detecting:
        cv2.rectangle(imaging_rgb,(a, b),
                        (a + height, b + width),
                        (0, 275, 0), 9)
pltd.subplot(1, 1, 1)
pltd.imshow(imaging_rgb)
pltd.show()