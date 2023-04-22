import cv2


class QRCodeError(Exception):
    pass


#  detect and decode qr code
def dad_qr(
        path
):
    try:
        image = cv2.imread(path)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(image)
        return value
    except:
        raise QRCodeError
