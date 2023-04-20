import cv2


class QRCodeError(Exception):
    pass


#  detect and decode qr code
def dad_qr(
        image
):
    try:
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(image)
        return value
    except:
        raise QRCodeError
