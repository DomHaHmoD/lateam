#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates
import csv

#recipients_list = ["dominique.hathi@gmail.com","maxime.girma@hotmail.fr","kev_wfc@hotmail.fr","raoultson@yahoo.fr"]
recipients_list = ["dominique.hathi@gmail.com"]
alerte_list = ['ferrari', 'tabouret']
#alerte_list = ['ferrari']
date = datetime.datetime.now()

def writehisto(recipients_list, alerte_list):

    #definiton de ce qu'il y a à écrire
    data = [alerte_list, recipients_list, date]

    # utilitaire pour écrire dans un file historique
    with open('historique.csv', 'wb') as csvfile:
        histo = csv.writer(csvfile, delimiter=',')
        #histo.writerow(alerte_list + [','] + recipients_list + [','] + date)
        for row in data:
            histo.writerow(row)

writehisto(recipients_list,alerte_list)
