import cv2
import easyocr as eo
import matplotlib.pyplot as pl

from static import PATH_TO_IMAGE, blur_par

reader = eo.Reader(['en'], gpu=True)


def detect_and_open_text(filename):
    #  start
    image = cv2.cvtColor(cv2.imread(PATH_TO_IMAGE + filename), cv2.COLOR_BGR2RGB)
    sh = image.shape
    img = image.copy()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    par0, par1 = blur_par(sh[0]), blur_par(sh[1])

    img = cv2.GaussianBlur(img, (par0, par1), 0)

    # _, img = cv2.threshold(img, 80, 200, cv2.ADAPTIVE_THRESH_MEAN_C)

    #  reading
    text = reader.readtext(img)
    for t in text:
        box, text, score = t
        cv2.rectangle(img, [int(i) for i in box[0]], [int(i) for i in box[2]], (255, 255, 0))
        cv2.putText(img, text, [int(i) for i in box[0]], cv2.FONT_HERSHEY_COMPLEX, 1, (225, 0, 0), 2)

    # output
    pl.imshow(img)
    pl.show()
