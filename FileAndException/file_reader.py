# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 13:52:45
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 14:04:18
# @Email: 749243884@qq.com
with open('pi_digits.txt') as file_object:
    #contents = file_object.read()
    # print(contents.rstrip())
    # for line in file_object:
    #    print(line.rstrip())

    lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
    print(pi_string)
    print(len(pi_string))
    pi = float(pi_string)
    print(pi * 64)
