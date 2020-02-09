#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    【简介】
	ui转换成py的转换工具

'''

import os
import os.path

# UI文件所在的路径
dir = './'

# 列出目录下的所有ui文件，並加入到list中回傳給呼叫Function
def listUiFile():
	list = []
	#print(dir)
	files = os.listdir(r"C:/python/aooi040/")
	for filename in files:
		#print( dir + os.sep + f  )
		#print(filename)
		if os.path.splitext(filename)[1] == '.ui':
			list.append(filename)
	print("ui:"+str(list))
	return list

# 把后缀为ui的文件改成后缀为py的文件名
def transPyFile(filename):
	return os.path.splitext(filename)[0] + '.py'

# 把后缀为ui的文件改成后缀为py的文件名
def transPy2File(filename):
	return os.path.splitext(filename)[0] + '_rc.py'

# 调用系统命令把ui转换成py
def runMain():
	list = listUiFile()
	for uifile in list :
		pyfile = transPyFile(uifile)
		cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)
		print(cmd)
		os.system(cmd)

# 列出目录下的所有ui文件
def listRcFile():
	list = []
	#print(dir)
	files = os.listdir(r"C:/python/aooi040/")
	for filename in files:
		#print( dir + os.sep + f  )
		#print(filename)
		if os.path.splitext(filename)[1] == '.qrc':
			list.append(filename)
	print("qrc:"+str(list))
	return list


# 调用系统命令把qrc转换成_rc.py
def runMain2():
	list = listRcFile()
	for rcfile in list :
		pyfile = transPy2File(rcfile)
		#cmd = 'pyrcc5 aooi040.qrc -o aooi040_rc.py'
		cmd = 'pyrcc5 {rcfile} -o {pyfile}'.format(pyfile=pyfile,rcfile=rcfile)
		print(cmd)
		os.system(cmd)

###### 程序的主入口
if __name__ == "__main__":
	runMain()
	runMain2()
