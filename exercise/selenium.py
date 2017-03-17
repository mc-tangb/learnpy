#!/usr/bin/env python
# --*-- encoding=utf-8 --*--
from urllib import request
import os
import re
import sys

def getpage(page=1):
	html_buf = request.urlopen("http://jandan.net/ooxx/page-" + str(page) + "#comments").read()
	html_buf = str(html_buf)
	imgs_pattern = r'//(([a-z0-9A-Z]|\/|\.)+?\.(png|jpg|jpeg))'
	imgs_list = re.findall(imgs_pattern, html_buf)
	return imgs_list

def saveImg(list):
	if not os.path.exists('./images'):
		os.mkdir('./images')
	img_name = re.compile(r'([a-z0-9A-Z]+?\.(png|jpg|jpeg)$)')
	for img in list:
		match = img_name.search(img[0])
		if match is not None:
			name = match.group()
			print('http://' + img[0])
			try:
				imgbuf = request.urlopen('http://' + img[0]).read()
				f = open('./images/' + name, 'wb')
				f.write(imgbuf)
				f.close()
				imgbuf = None
			except Exception as err:
				pass
			finally:
				pass

if __name__ == '__main__':
	for m in [i for i in range(int(sys.argv[1])) if i>0]:
		list = getpage(m)
		saveImg(list)
	
