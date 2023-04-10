PATH_TO_IMAGE = 'static/img/'
PATH_TO_RESULT = 'static/result/'


def blur_par(num: int) -> int:
    return num // 800 * 2 + 1


def kernel_par(num: int) -> int:
    return num // 1000 * 2 + 1
