#Les 4 fonctions qui suivent returnent True ou une liste permettant au main de continuer
#Elles n'ont aucune fonction réelle

def test_conf():
    return True

def send_mail(x,y,z):
    return True

#import des fichiers .py
from blescan import *

#import des biblios
from bluepy.btle import Scanner, DefaultDelegate
import time

# Déclaration des objets utiles au programme:

global_list = []    #liste des appareils bluetooth scannés par le BLE
sensors_list = get_sensors_data()   #liste des objets capteurs déployés (sensors_conf.py)
alert_list = []     #liste des capteurs détectés lors du scan (blescan.py/mac_filter())
mail_sended = False #bool pour savoir si le mail est bien parti
waiting_list = []   #liste d'attente contenant les capteurs pour qui le mail n'a pas pu être envoyé
recipients_list = get_recipients_data()  #liste des destinataires des mails d'alerte (recipients_conf.py)
alert_frequence = 0      #fréquence d'alerte choisie par l'utilisateur RECUP DANS CSV!!!!

if test_conf() : #si le test renvoie vrai on peut y aller, sinon, on quitte le main

#    load_conf() # servira à charger la conf dans les variable déclarées plus haut
#    send_statut() # éventuellement pour alerter que le systeme à bien demarré

    while True: # A partir d'ici le programme tournera jusqu'a l'arret du rasp

        global_list = bluetooth_scan() #On recupere notre liste d'objets scannés

        if global_list == None: #On s'assure qu'il y a quelque chose
            time.sleep(5) # On attend 5 sec avant de relancer le scan blutooth
            continue

        sensors_mac_list = []        # on récupère la liste des mac des capteurs déployés dans la liste d'objets
        for sensors_object in sensors_list
            sensors_mac_list.append(sensors_object.mac)

        alert_list = mac_filter(global_list,sensors_mac_list) # on crée notre liste d'alerte
        if alert_list == None: #si ya rien on rescanne immediatement
            continue
        mail_sended = send_mail(alert_list,recipients_list,waiting_list) #TODO doit send 1 seul mail pour plusieurs capteurs

        if mail_sended :
            for sensor in sensors_list:
                if sensor in alert_list:
                    sensor.last_alert = time.time()#mise à jour de la derniere alerte
                if sensor in waiting_list:
                    sensor.last_alert = time.time()#pareil

                write_histo(alert_list,waiting_list)#ecrit le nom du capteur et l'heure actuelle dans l'histo

            for sensor in waiting_list: #le mail est parti avec la waiting list, donc on peut la del
                del sensor

        else:                           #si le mail a échoué
            for mac_alert in alert_list
                waiting_list.append(mac_alert)#ajout des alertes a la waiting list pour le prochain tour


#else:
#    return 0

#les deux dernieres lignes sont commenté pour le moment car sinon ca fait planter le script.
# (pas de return sur la "racine")
