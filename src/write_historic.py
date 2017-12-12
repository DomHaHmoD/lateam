#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates
import csv

"""recipients_list = ["dominique.hathi@gmail.com","maxime.girma@hotmail.fr","kev_wfc@hotmail.fr","raoultson@yahoo.fr"]
#recipients_list = ["dominique.hathi@gmail.com"]
alert_list = ["ferrari","tabouret"]"""



def write_histo(recipients_list, final_alert_list):

    date = str(datetime.datetime.now())

    #definiton de ce qu'il y a à écrire
    #data = [final_alert_list, recipients_list, date]
    name_list = []
    for item in final_alert_list:
        name_list.append(item.name)



    data = [name_list,recipients_list,date]
    print(data)

    # utilitaire pour écrire dans un file historique
    with open('historique.csv','a') as csvfile:
        newFileWriter = csv.writer(csvfile)
        newFileWriter.writerow(data)
        print('yess write')

    return
