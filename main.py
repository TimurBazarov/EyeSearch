from text_detecting import detect_and_open_text
from dad_qr import dad_qr


def test1():
    detect_and_open_text('img1.png')
    detect_and_open_text('img2.png')
    detect_and_open_text('img3.png')


def test2():
    print(dad_qr('qr_code1.png'))  # 100,20,40,60,20,px
    print(dad_qr('qr_code2.png'))  # a funny cow


# test1()
test2()
