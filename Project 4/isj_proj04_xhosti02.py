#!/usr/bin/env python3

#Adam Hostin
#27.3.2018
#proj č.4 ISJ(skriptovacie jazyky)

def can_be_a_set_member_or_frozenset(item):
    """function returns item if it could be member of set else return frozenset(item)
    item could be an element of set if it is an int or a tuple"""

    if type(item) is tuple:
        return item
    elif type(item) is int:
        return item
    else:
        return frozenset(item)

def all_subsets(lst):
    """function returns potential set of a lst"""

    result=[[]]
    for elem in lst:
        result.extend([x + [elem] for x in result])
    return result


def all_subsets_excl_empty(*arg,**exclude):
    """function calls all_subsets(lst) for n elements of a list
    :returns potential set of a list if exclude empty is False else returns potential set"""

    lst=list(arg)

    result=all_subsets(lst)

    if (exclude == {})or(exclude['exclude_empty'] == True):
        result.pop(0)

    return result

