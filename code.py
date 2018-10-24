#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import quote, unquote
//解决API中url传参中文乱码问题
def test():
    a="你好"
    b="测试"
    c="我问他"
    name =quote(c,"gbk")
    name =quote(name,'gbk')
    #url = "https://172.19.38.133/login?admin="+name+"&pwd=talent&role=access&token=true"
    print name

test()
