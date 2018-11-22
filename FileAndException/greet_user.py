# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 15:23:37
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 15:27:03
# @Email: 749243884@qq.com
import json
filename = 'username.json'
with open(filename) as file_obj:
    username = json.load(file_obj)
    print("Welcome back, " + username + "!")
