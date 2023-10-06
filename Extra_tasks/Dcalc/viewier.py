from Extra_tasks.Dcalc.dcalc import deg_to_gms


def compare_points_gms(*args, **kwargs) -> list[str]:
    """
    :param args: набор десятичных градусов, который будет добавлен в начало набора именованных градусов (kwargs)
    с именами по шаблону "Point_{i}", где i - индекс градуса в args
    :param kwargs: набор именованных десятичных градусов
    :return: список строк по шаблону "{name_deg} = ГГ° ММ′ СС", где name_deg - это имя именованного градуса
    """
    points_deg = {f"Point_{i}": e for i, e in enumerate(args)}
    points_deg.update(kwargs)
    return [f"{name} = {deg_to_gms(points_deg[name])}" for name in points_deg]


if __name__ == "__main__":
    print(compare_points_gms(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put=140.85706440))
