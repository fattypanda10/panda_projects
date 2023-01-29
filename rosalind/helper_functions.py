""" Helper functions for Rosalind Problems """


def order_dict_by_key(dictionary: dict) -> list:
    return sorted(dictionary.items(), key=lambda x: x[0])
