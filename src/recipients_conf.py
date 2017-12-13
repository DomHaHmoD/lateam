'''
KevinGeorget
11/12/2017
version 0.9

get_recipient_data() ouvre un fichier CSV contenant les destinataires et en renvoie la liste
à la fonction MAIN.
'''

import csv

def get_recipients_data():

    with open('recipients_conf.csv') as file:     #ouverture du CSV config
        recipients_raw_list = list(csv.reader(file, delimiter=','))  #création d'une liste de 2 listes

    recipients_list = recipients_raw_list[1] #on recupere la liste de mail
    recipients_list = recipients_list[1:]       #on tronque la premiere colonne

    return recipients_list

print(get_recipients_data()) #test
