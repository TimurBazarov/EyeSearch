def test1():
    from text_detecting import show_text_from, detect_text

    print(detect_text('img1.png'))
    print(detect_text('img2.png'))
    print(detect_text('img3.png'))
    # show_text_from('eq2.png')


def test2():
    from dad_qr import dad_qr

    print(dad_qr('qr_code1.png'))  # 100,20,40,60,20,px
    print(dad_qr('qr_code2.png'))  # a funny cow


def test3():
    from eq_solve import das_eq

    print(das_eq('eq1.png'))
    print(das_eq('eq2.png'))
    print(das_eq('eq3.png'))


# test1()
# test2()
test3()
