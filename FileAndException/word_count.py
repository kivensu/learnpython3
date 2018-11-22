# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 14:53:10
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 15:03:29
# @Email: 749243884@qq.com


def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        #msg = "The file " + filename + " does not exist!"
        # print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words")


filenames = ['programming.txt', 'guest.txt', '1.txt']
for filename in filenames:
    count_words(filename)
