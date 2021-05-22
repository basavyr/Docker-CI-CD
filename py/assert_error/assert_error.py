#!/usr/bin/env python

import sys

cli_number = 1

try:
    cli_number = sys.argv[1]
except:
    pass
    # print(f'no cli number give. defaulting to {cli_number}')
else:
    # print(f'CLI number was {cli_number}')
    pass


try:
    assert cli_number == 1, 'no good'
except AssertionError:
    print(f'no default number. will use the cli one ->{cli_number}')
else:
    print(f'all good -> {cli_number}')
