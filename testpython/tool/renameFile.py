# coding=utf-8
import os
import re

path = '/home/liunian/桌面/Palette/drawable'
i = 1;
for file in os.listdir(path):
	if os.path.isfile(os.path.join(path,file))==True:
		suffix = file.split(".")[1]
		oldname = path + "/" + file
		newname = path + "/" + "img_" + str(i) + "." + suffix
		print (newname)
		os.renames(oldname, newname)
		i = i + 1
