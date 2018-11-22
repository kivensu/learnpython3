# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 15:10:14
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 15:11:34
# @Email: 749243884@qq.com
import json
filename = 'number.json'
with open(filename) as file_obj:
    number = json.load(file_obj)
print(number)
