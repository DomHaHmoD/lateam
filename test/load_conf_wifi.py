#necessité de rebooter pour charger la nouvelle config.

import csv

def get_conf_wifi():
    return_list = []
    with open('config_wifi.csv') as file: # ouverture du csv
        temporary_list = list(csv.reader(file,delimiter=","))

        return_list.append(temporary_list[0][1])
        return_list.append(temporary_list[1][1])
        return_list.append(temporary_list[2][1])

    return return_list

def config_wpa_supplicant(wifi_SSID,wifi_PASSWRD,wifi_safety_type):
    connect_login = []
    connect_login.append("network={\n")
    connect_login.append('ssid="{}"\n'.format(wifi_SSID))
    connect_login.append('psk="{}"\n'.format(wifi_PASSWRD))
    connect_login.append("key_mgmt={}\n".format(wifi_safety_type))
    connect_login.append("}")

    #effacer l'ancien fichier?
    fichier_wpa = open("test_login","a")##/etc/wpa_supplicant/wpa_supplicant.conf
    for elements in connect_login:
        fichier_wpa.write(elements)
    fichier_wpa.close()

temporary_list = get_conf_wifi()

wifi_SSID = temporary_list[0] #les deux variables sont des str
wifi_PASSWRD = temporary_list[1]
wifi_safety_type = temporary_list[2]

config_wpa_supplicant(wifi_SSID,wifi_PASSWRD,wifi_safety_type)

#/etc/wpa_supplicant/wpa_supplicant.conf
