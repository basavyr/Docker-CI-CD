#!/usr/bin/env python
import numpy as np

my_list = [1, 2, 3]


def insert_element(pos, element, lister):
    try:
        lister.insert(pos, element)
    except Exception as exc:
        print(
            f'Could not insert the element {element} at position {pos} in the list: {lister}')
    else:
        pass
    return


print(my_list)
insert_element(1, 1, my_list)
print(my_list)
