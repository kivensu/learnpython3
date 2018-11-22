# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 14:31:25
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 14:49:00
# @Email: 749243884@qq.com
"""
try:
	print(5 / 0)
except ZeroDivisionError:
	print ("You can't divide by zero!")
"""
print("Give me two numbers, and I will divide them!")
print("Enter 'q' to quit!")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = first_number / second_number
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
