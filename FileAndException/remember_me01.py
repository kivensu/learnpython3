# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 15:27:42
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 15:32:00
# @Email: 749243884@qq.com
import json
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What you name:")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back," + username + "!")
else:
    print("Welcome back," + username + "!")
