# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 14:06:34
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 14:11:58
# @Email: 749243884@qq.com
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating a new games!\n")

with open(filename, 'a') as file_object01:
	file_object01.write("I also love finding meaning in large datasets.\n")