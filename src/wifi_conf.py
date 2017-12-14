'''
maximeGirma
14/12/2017
version 0.5
La fonction recupere le fichier de configuration wifi, regarde si le précendent fichier
est différent, si c'est le cas elle charge le nouveau et redemmare pour charger la nouvelle
configuration.
'''
import os
import csv
from .conf import DATA_DIR
def get_conf_wifi():
    return_list = []
    with open(DATA_DIR + '/config_wifi.csv') as file: # ouverture du csv
        temporary_list = list(csv.reader(file,delimiter=","))

        return_list.append(temporary_list[0][1])
        return_list.append(temporary_list[1][1])
        return_list.append(temporary_list[2][1])
        print (return_list)
    return return_list

def config_wpa_supplicant(wifi_SSID,wifi_PASSWRD,wifi_safety_type):
    connect_login = 'country=GB\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n'
    connect_login +='update_config=1\n\nnetwork={\n\t'
    connect_login +='ssid="{}"\n\tpsk="{}"\n\t'.format(wifi_SSID,wifi_PASSWRD)
    connect_login +='key_mgmt={}\n'.format(wifi_safety_type)
    connect_login +='}'

    with open("/etc/wpa_supplicant/wpa_supplicant.conf","r") as fichier_wpa:
        wpa_original = fichier_wpa.read()

    if wpa_original != connect_login:

        with open("/etc/wpa_supplicant/wpa_supplicant.conf","w") as fichier_wpa:
            fichier_wpa.write(connect_login)
        os.system("sudo reboot")

temporary_list = get_conf_wifi()

wifi_SSID = temporary_list[0] #les deux variables sont des str
wifi_PASSWRD = temporary_list[1]
wifi_safety_type = temporary_list[2]

config_wpa_supplicant(wifi_SSID,wifi_PASSWRD,wifi_safety_type)
