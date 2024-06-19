import collections
from collections import Counter
import re


def executed_dicts(dicts: list, state: str = "EXECUTED") -> list:
    """Функция которая принимает список словарей и значение ключа ' state '
    и возвращает список словарей содержащих переданное ключу значение"""

    new_dict_list = []
    for dict_ in dicts:
        if "state" in dict_:
            if dict_["state"] == state:
                new_dict_list.append(dict_)
        else:
            new_dict_list.append([])
    return new_dict_list


def sorted_dicts(dicts: list, reverse: bool = True) -> list:
    """Фунция принимает список словарей и возвращает отсортированный список словарей по дате"""
    not_empty_dicts = []
    for dict in dicts:
        if "date" in dict:
            not_empty_dicts.append(dict)
    sorted_dicts_list = sorted(not_empty_dicts, key=lambda key: key["date"], reverse=reverse)
    return sorted_dicts_list


def filter_dicts_by_string(dicts_to_filter, string):
    """Функция принимает список словарей с данными о транзакциях и строку для поиска, и возвращает список словарей,
    в которых присутствет строка для поиска"""

    filtered_dicts_list = []
    for dict in dicts_to_filter:
        if "description" in dict:
            match = re.findall(rf"{string}+", dict["description"], re.IGNORECASE)
            if match:
                filtered_dicts_list.append(dict)
    return filtered_dicts_list


def sort_dicts_by_categories(list_of_dicts, list_of_categories):
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в которой ключи - категории операций, а значения - количества транзакций
    в каждой из перечислинных категорий"""

    descriptions = [dict_["description"] for dict_ in list_of_dicts]
    descriptions_counted = Counter(descriptions)
    my_dict = collections.defaultdict(int)
    for i in range(len(list_of_categories)):
        my_dict[list_of_categories[i]] = descriptions_counted[list_of_categories[i]]
    return my_dict
