def executed_dicts(dicts: list, state: str = "EXECUTED") -> list:
    """Функция которая принимает список словарей и значение ключа ' state '
    и возвращает список словарей содержащих переданное ключу значение"""

    new_dict_list = []
    for dict_ in dicts:
        if dict_["state"] == state:
            new_dict_list.append(dict_)
    return new_dict_list
