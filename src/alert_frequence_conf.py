'''
MaximeGirma 13/12/2017 -- 11H51 -- Version ?
alert_frequence_conf.py contient la fonction get_alert_frequence_data()
Cette fonction ouvre le fichier de configuration nommé "alert_frequence.csv" et en sctocke le contenu
Ce contenu servira à définir le temps minimal à respecter entre deux alertes.
Si le fichier de configuration est vide ou contient des élements invalide
une valeur par defaut sera utilisée(60)

Cette valeur est ensuite renvoyée à la fonction main.
'''


import csv
def get_alert_frequence_data():
    alert_frequence = 0

    try:
        with open('alert_frequence.csv') as file: # ouverture du csv
            temporary = list(csv.reader(file))# les 3 lignes suivantes servent à recuperer un int en le sortant
            temporary2 = temporary[0]#          par à coup de la double liste
    except FileNotFoundError:
        alert_frequence = 60
        print("NO ALERT_FREQUENCE.CSV")
        return alert_frequence

    try:
        alert_frequence = int(temporary2[0]) #On verifie que la valeur est un entier
    except ValueError:
        alert_frequence = 60 #assignation valeur par défaut

    if alert_frequence < 0: # on verifie que l'entier est positif
        alert_frequence = 60;#assignation valeur par defaut

    print(alert_frequence,"est la frequence d'alerte")#print de test
    return alert_frequence
