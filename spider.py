# -*- coding: utf-8 -*-
#author yb
#抓取链家北京的每天的二手房数据
from urllib2 import urlopen

from bs4 import BeautifulSoup
import time
while True:
	url = "https://bj.lianjia.com/ershoufang/"
	#url = "https://tj.lianjia.com/ershoufang/"
	content = urlopen(url)
	bsObj=BeautifulSoup(content)
	info=bsObj.findAll("div",{"class":"resultDes clear"})
	print time.strftime('%Y-%m-%d', time.localtime()),info[0].text
	data = info[0].text[3:10]
	s = time.strftime('%Y-%m-%d', time.localtime()) + "   " + data+"\n"
	with open("/home/yb/house.txt", 'a+') as f:
		f.write(s)
	time.sleep(60*60*24)
