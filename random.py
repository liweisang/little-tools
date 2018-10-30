# -*- coding: utf-8 -*-
import random
import string
def zifu():
    seed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+-=<>?"
    sa = []
    for i in range(10):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt
#获取没有“+”的十位随机字符串
def test():
    sign = zifu()
    while "+" in sign:
        sign = zifu()
        print sign


    print "11111111111",sign
test()
