#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates

# utilitaire pour ouvrir un file destinataires
"""dest = open('filetestaecrire', 'r')
destfinal = dest.read()
destinataires = destinataires.split("\n")
d1 = ', '.join(destinataires)"""

datatoinsert = ['cafetière', 'ferrari', 'pcportable', 'jaguar', 'aston']
datatoinsert2 = ['00:1A:2B:3C:5E', '00:4A:3B:3C:4B', '00:5A:0B:8C:3C', '00:6A:4B:1C:1C', '00:7A:8B:9C:6F']

# utilitaire pour écrire dans un file historique
destfinal = open('filetestaecrire', 'a')
# utilitaire de gestion des dates
date = datetime.datetime.now()
for a,b in zip(datatoinsert,datatoinsert2):
	#i=0; i=i+1
	#destfinal.write("""Descriptif du matériel protégé:
#capteur{i}={}={}


#""" + str(date)) # le \n pour un saut de ligne
	print('capteur={}={}.'.format(a,b))
destfinal.close()
