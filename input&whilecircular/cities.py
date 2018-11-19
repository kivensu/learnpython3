# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-19 16:13:28
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-19 16:18:21
# @Email: 749243884@qq.com
prompt = "\nPlease enter the name of city you hava visted: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = str(input(prompt))
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
