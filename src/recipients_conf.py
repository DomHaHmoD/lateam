'''
KevinGeorget
11/12/2017
version 0.9

get_recipient_data() ouvre un fichier CSV contenant les destinataires et renvoie la liste
d'email à la fonction MAIN.
'''

import csv

def get_recipients_data():

    recipients_list = []

    with open('recipients_conf.csv') as file:     #ouverture du CSV config
        recipients = csv.reader(file, delimiter=',')
        file.readline() # on consomme la 1ere ligne (entrées tableau)

        for raw in recipients:              #pour chaque ligne on ajoute les adresses mail dans la liste
            recipients_list.append(raw[1])

    return recipients_list

print(get_recipients_data()) #test
