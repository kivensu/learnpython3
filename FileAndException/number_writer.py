# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 15:07:34
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 15:09:45
# @Email: 749243884@qq.com
import json
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filename = 'number.json'
with open(filename, 'a') as file_obj:
    json.dump(numbers, file_obj)
