'''
KevinGeorget
11/12/2017
version 0.9

get_recipient_data() ouvre un fichier CSV contenant les destinataires et renvoie la liste
d'email à la fonction MAIN.
'''

import csv
from .conf import DATA_DIR


def get_recipients_data():

    recipients_list = []

<<<<<<< HEAD
    with open(DATA_DIR + '/recipients_conf.csv') as file:     #ouverture du CSV config
=======
    with open('recipients_conf.csv') as file:     # ouverture du CSV config
>>>>>>> 518984f1ed6e5d1754ba2a0c2c21ce633d750803
        recipients = csv.reader(file, delimiter=',')
        file.readline()  # on consomme la 1ere ligne (entrées tableau)

        for row in recipients:              # pour chaque ligne on ajoute les adresses mail dans la liste
            recipients_list.append(row[1])

    return recipients_list


print(get_recipients_data())  # test
