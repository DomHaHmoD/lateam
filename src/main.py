#Les 4 fonctions qui suivent returnent True ou une liste permettant au main de continuer
#Elles n'ont aucune fonction réelle




#import des fichiers .py
from blescan import *
from alert_frequence_conf import *
from recipients_conf import *
from sensors_conf import *
from notify import *
from update_sensors_list import *
from test_conf import *
from notify import *
from write_historic import *
#import des biblios
from bluepy.btle import Scanner, DefaultDelegate
import time
import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Déclaration des objets utiles au programme:

global_list = []    #liste des appareils bluetooth scannés par le BLE
sensors_list = get_sensors_data()   #liste des objets capteurs déployés (sensors_conf.py)
alert_list = []     #liste des capteurs détectés lors du scan (blescan.py/mac_filter())
mail_sended = False #bool pour savoir si le mail est bien parti
waiting_list = []   #liste d'attente contenant les capteurs pour qui le mail n'a pas pu être envoyé
recipients_list = get_recipients_data()  #liste des destinataires des mails d'alerte (recipients_conf.py)
alert_frequence = get_alert_frequence_data()      #fréquence d'alerte choisie par l'utilisateur RECUP DANS CSV!!!!

if test_conf() : #si le test renvoie vrai on peut y aller, sinon, on quitte le main

#    load_conf() # servira à charger la conf dans les variable déclarées plus haut
#    send_statut() # éventuellement pour alerter que le systeme à bien demarré

    while True: # A partir d'ici le programme tournera jusqu'a l'arret du rasp
        print("on est dans la boucle")
        global_list = bluetooth_scan() #On recupere notre liste d'objets scannés

        if len(global_list) == 0: #On s'assure qu'il y a quelque chose
            time.sleep(5) # On attend 5 sec avant de relancer le scan blutooth
            continue

        alert_list = mac_filter(global_list, sensors_list) # on crée notre liste d'alerte en filtrant une premiere fois

        if len(alert_list) == 0: #si ya rien on rescanne immediatement
            continue

        final_alert_list = time_filter(alert_list) #filtre en fonction de la derniere alerte

        mail_sended = notify(recipients_list, final_alert_list, alert_frequence)

        if mail_sended:

            sensors_list = update_sensors_list(sensors_list, final_alert_list)#met a jour le item.last_alert

            write_histo(recipients_list, final_alert_list)#ecrit le nom du capteur et l'heure actuelle dans l'histo

            for sensor in waiting_list: #le mail est parti avec la waiting list, donc on peut la del
                del sensor

        else:                           #si le mail a échoué
            for alert in final_alert_list:
                waiting_list.append(alert)#ajout des alertes a la waiting list pour le prochain tour


#else:
#    return 0

#les deux dernieres lignes sont commenté pour le moment car sinon ca fait planter le script.
# (pas de return sur la "racine")
