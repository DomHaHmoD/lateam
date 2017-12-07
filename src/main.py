#Les 4 fonctions qui suivent returnent True ou une liste permettant au main de continuer
#Elles n'ont aucune fonction réelle

def test_conf():
    return True
def scanner():
    return [12345,67890,54321]

def filter(x,y):
    return [12345]
def send_mail(x,y,z):
    return True

#import des fichiers .py
import blescan.py

#import des biblios
from bluepy.btle import Scanner, DefaultDelegate
import time
# Déclaration des listes et variables utiles au programme
global_list = []
alert_list = []
sensors_list = []
mail_sended = False #bool pour savoir si le mail est bien parti
waiting_list = []
destinataires_list = []
alert_frequence = 0
i = 0 # sert pour un while, je galère avec les for in.

if test_conf() : #si le test renvoie vrai on peut y aller, sinon, on quitte le main

#    load_conf() # servira à charger la conf dans les variable déclarées plus haut
#    send_statut() # éventuellement pour alerter que le systeme à bien demarré

    while True: # A partir d'ici le programme tournera jusqu'a l'arret du rasp

        global_list = bluetooth_scan() #On recupere notre liste d'objets scannés

        if global_list == None: #On s'assure qu'il y a quelque chose
            time.sleep(5) # On attend 5 sec avant de relancer le scan blutooth
            continue
        alert_list = filter(global_list,sensors_list) # on crée notre liste d'alerte
        if alert_list == None: #si ya rien on rescanne immediatement
            continue
        mail_sended = send_mail(alert_list,destinataires_list,waiting_list)

        if mail_sended :
            for sensor in sensors_list:
                if sensor.mac in alert_list:
                    sensor.last_alert = time.time()#mise à jour de la derniere alerte
                elif sensor.mac in waiting_list:
                    sensor.last_alert = time.time()#pareil

                write_histo(alert_list,waiting_list)#ecrit le nom du capteur et l'heure actuelle dans l'histo

            for sensor in waiting_list: #le mail est parti avec la waiting list, donc on peut la del
                del sensor

        else:#si le mail a échoué
            while i < len(alert_list):
                waiting_list.append(alert_list[i])#ajout des alertes a la waiting list pour le prochain tour
                i += 1
            i = 0
#else:
#    return 0

#les deux dernieres lignes sont commenté pour le moment car sinon ca fait planter le script.
# (pas de return sur la "racine")
