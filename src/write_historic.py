#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates
import csv

"""recipients_list = ["dominique.hathi@gmail.com","maxime.girma@hotmail.fr","kev_wfc@hotmail.fr","raoultson@yahoo.fr"]
#recipients_list = ["dominique.hathi@gmail.com"]
alert_list = ["ferrari","tabouret"]"""

date = str(datetime.datetime.now())

def write_histo(recipients_list, alert_list):

    #definiton de ce qu'il y a à écrire
    #data = [alert_list, recipients_list, date]
    data = [alert_list,recipients_list,date]
    print(data)

    # utilitaire pour écrire dans un file historique
    with open('historique.csv','a') as csvfile:
        newFileWriter = csv.writer(csvfile)
        newFileWriter.writerow(data)
        print('yess write')
