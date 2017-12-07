#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates

# utilitaire pour ouvrir un file coniguration
"""conf = open('configuration', 'r')
conf = conf.read()
conf = conf.split("\n")
conf = ', '.join(conf)"""

datatoinsert = ['00:1A:2B:3C:5E', '00:4A:3B:3C:4B', '00:5A:0B:8C:3C', '00:6A:4B:1C:1C', '00:7A:8B:9C:6F']
macorigin = '00:1A:2B:3C:5E'

# utilitaire pour testter si une mac est connue et écrire dans un file filemacteste
f1 = open('filemacteste', 'w')
# utilitaire de gestion des dates
date = datetime.datetime.now()
f1.write("[")
for mac in datatoinsert:
	if macorigin == mac:
		print('vrai')
		f1.write("'" + mac + "'" + ",vrai," + str(date) + ",\n")
	# si on ne veut pas écrire le adresse non connue, il faut commenter les lignes else
	else:
		print('faux')
		f1.write(mac + ",faux,\n")

f1.write("]")
f1.close()


