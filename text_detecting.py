import cv2
import easyocr as eo
import matplotlib.pyplot as pl


def blur_par(num):
    return num // 800 * 2 + 1


PATH_TO_IMAGE = 'static/img/'


def open_detected_text(filename):
    #  start
    image = cv2.cvtColor(cv2.imread(PATH_TO_IMAGE + filename), cv2.COLOR_BGR2RGB)
    sh = image.shape
    img = image.copy()
    par0, par1 = blur_par(sh[0]), blur_par(sh[1])
    img = cv2.GaussianBlur(img, (par0, par1), 0)

    #  thresholding

    _, img = cv2.threshold(img, 80, 200, cv2.ADAPTIVE_THRESH_MEAN_C)

    #  reading
    reader = eo.Reader(['en'], gpu=True)

    text = reader.readtext(img)
    for t in text:
        box, text, score = t
        cv2.rectangle(image, [int(i) for i in box[0]], [int(i) for i in box[2]], (255, 255, 0))
        cv2.putText(image, text, [int(i) for i in box[0]], cv2.FONT_HERSHEY_COMPLEX, 1, (225, 0, 0), 2)

    # output
    pl.imshow(image)
    pl.show()
