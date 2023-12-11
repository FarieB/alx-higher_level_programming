#!/usr/bin/python3
# -----------------------------------------------------------
# Python function that:
# function that returns a list with all values multiplied by a number
# withouth using any loops
#
# (C) 2023 Farai Bande, South Africa
# email igbinijesusamuel@gmail.com
# -----------------------------------------------------------


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda i: number * i, my_list))
