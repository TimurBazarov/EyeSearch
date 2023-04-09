import cv2
from static import PATH_TO_IMAGE


class QRCodeError(Exception):
    pass


def dad_qr(filename):
    try:
        image = cv2.imread(PATH_TO_IMAGE + filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(image)
        return value
    except:
        raise QRCodeError
