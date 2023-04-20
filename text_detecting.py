import cv2
# import easyocr as eo

from static import blur_par

reader = eo.Reader(['en'], gpu=True)


def detect_text(image) -> list:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    sh = image.shape
    img = image.copy()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    par0, par1 = blur_par(sh[0]), blur_par(sh[1])

    img = cv2.GaussianBlur(img, (par0, par1), 0)

    # _, img = cv2.threshold(img, 80, 200, cv2.ADAPTIVE_THRESH_MEAN_C)

    #  reading
    result = reader.readtext(img)
    text = []
    for t in result:
        box, data, score = t
        text.append(data)

    return text


def show_text_from(img):
    text = detect_text(img)
    return text
