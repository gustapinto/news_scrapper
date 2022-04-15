from collections.abc import Iterable


def flatten(t: list) -> list:
    return [a for b in t for a in b]

def remove_none_entries(var: Iterable) -> Iterable:
    if type(var) is list:
        return [e for e in var if e]

    if type(var) is dict:
        return {k: var[k] for k in var if k and var[k]}
