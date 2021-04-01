# -*- coding: utf-8 -*-
print("１行１文字 abc")
input_data = input()
print("input is : " + input_data)

print("１行１数字 99")
input_data = int(input())
print("input is : " + str(input_data))

print("１行n文字  abc def ghi")
a, b, c = input().split()
print("input is : " + a)
print("input is : " + b)
print("input is : " + c)