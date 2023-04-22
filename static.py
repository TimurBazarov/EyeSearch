PATH_TO_IMAGE = 'static/img/source/'
PATH_TO_RESULT = 'static/result/'
PATH_TO_SOURCE = 'static/img/source/'


def blur_par(num: int) -> int:
    return num // 800 * 2 + 1


def kernel_par(num: int) -> int:
    return num // 1000 * 2 + 1
