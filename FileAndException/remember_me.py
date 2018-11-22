# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 15:12:52
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 15:27:00
# @Email: 749243884@qq.com
import json
username = input("What's you name: ")
filename = "username.json"
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back " + username + "!")
