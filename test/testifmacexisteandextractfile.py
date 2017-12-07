#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates

listeglobale = ['00:1A:2B:3C:5E', '00:4A:3B:3C:4B', '00:5A:0B:8C:3C', '00:6A:4B:1C:1C', '00:7A:8B:9C:6F']

# utilitaire pour ouvrir un file coniguration
listecapteur = []
listecapteur = open('capteurs','r')
listecapteur = listecapteur.read()
print(listecapteur)

macorigin = '00:1A:2B:3C:5E'

# utilitaire pour tester si une mac est connue et écrire dans un file filemacteste
f1 = open('filealerte', 'w')

# utilitaire de gestion des dates
date = datetime.datetime.now()

#f1.write("[")
for mac in listeglobale:
	if macorigin == mac:
		print('vrai')
		for i,j in listecapteur:
			for k,l in (listecapteur(i)):
				print(l)
				print(macorigin)
				if l == macorigin:
					print(i,k)
				
					#f1.write("'" + macorigin[0] + "'," + macorigin[1] + "'" + ",vrai," + str(date) + ",")
					#f1.write("'" + macorigin[0] + "'," + ",vrai," + str(date) + ",")
					#f1.write("toto")

#f1.write("]")
#f1.close()
