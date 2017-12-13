'''
maximeGirma 11/12/2017 --
La fonction essaie de monter une clé usb durant 1 minute, ou jusqu'a qu'elle y arrive. Puis elle copie
les fichiers de conf de la clé dans son repertoire de travail.
la copie supprime les anciens fichiers si ils existent.
si il n'y a pas de fichiers ou pas de clé usb, les fichiers de conf précédents sont utilisés.
Si ils ne sont pas présents le programme s'arretera. Puis se relancera.'''


import os
from time import sleep

def auto_mount():

    print("on est dans automount")

    error_mount = 8192 # erreur renvoyée si il n'y a pas de clé usb
    compteur = 0
    while (error_mount == 8192) and (compteur < 10): #on essaye de monter une clé usb pendant une minute
        print("on monte la clef")
        error_mount = os.system("sudo mount /dev/sda /mnt/usbStick") #commande pour monter
        sleep(1)
        if error_mount == 8192:
            sleep(5)
            compteur+=1

    #copie des fichiers de conf

    os.system("cp -f /mnt/usbStick/recipients_conf.csv /home/pi/src/recipients_conf.csv")
    os.system("cp -f /mnt/usbStick/sensors_conf.csv /home/pi/src/sensors_conf.csv")
    os.system("cp -f /mnt/usbStick/alert_frequence.csv /home/pi/src/alert_frequence.csv")
    sleep(1)


    os.system("sudo umount /mnt/usbStick") #on demonte
