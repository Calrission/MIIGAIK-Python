from math import pi


def deg_to_gms(deg: float | int, format_result_is_str: bool = True) -> tuple[int, int, int] | str:
    """
    :param deg: Градусы в десятичном представлении
    :param format_result_is_str: Формат конечных данных - форматированная строка (=True) или кортеж из чисел (=False)
    :return: Градусы, минуты, секунды - по умолчанию в формате ГГ° ММ′ СС″
    """
    degrees = int(deg)
    minutes = int((deg - degrees) * 60)
    seconds = round(((deg - degrees) * 60 - minutes) * 60, 5)

    return f'{degrees}° {minutes}′ {seconds}″' if format_result_is_str else (degrees, minutes, seconds)


def gms_to_deg(degrees: int, minutes: int, seconds: int | float) -> float:
    """
    :param degrees: Градусы в целочисленном представлении
    :param minutes: Минуты в целочисленном представлении
    :param seconds: Секунды в целочисленном или десятичном представлении
    :return: Градусы в десятичном представлении
    """
    return degrees + (minutes / 60) + (seconds / 3600)


def deg_to_rad(deg: float) -> float:
    """
    :param deg: Градусы в десятичном представлении
    :return: Радианы в десятичном представлении
    """
    return deg * (pi / 180)


def rad_to_deg(rad: float) -> float:
    """
    :param rad: Радианы в десятичном представлении
    :return: Градусы в десятичном представлении
    """
    return rad * (180 / pi)
