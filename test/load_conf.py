
#def load_conf_destinataires:
import os
import csv
os.system("cp /media/maxime/*/destinataires.csv /home/maxime/Documents/projet_1/secure_stand/lateam/test/destinataires.csv")
list_destinataires = []
with open('destinataires.csv', newline = '') as file:
    list_temporaire = csv.reader(file)

    for element in list_temporaire:

        list_destinataires.append(element[1])

print(list_destinataires)
os.system("rm /home/maxime/Documents/projet_1/secure_stand/lateam/test/destinataires.csv")
#return list_destinataires

#def load_conf_capteurs
