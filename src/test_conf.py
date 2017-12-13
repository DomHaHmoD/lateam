import os

def test_conf_file():
    try:
        with open("recipients_conf.csv","r") as file:
            a = 0
            print("there is a recipient_conf.csv")
    except FileNotFoundError:
        return False

    try:
        with open("sensors_conf.csv","r") as file:
            a = 0
            print("there is a sensors_conf.csv")
    except FileNotFoundError:
        return False

    return True

def test_wifi():

    ping = os.system("ping 8.8.8.8 -c 1")
    if ping == 0:
        return True
    else :
        return False





def test_conf():


    is_conf_file_here = test_conf_file()
#    if is_conf_file_here is not True:
#        return False


    is_wifi_connected = False
    compteur = 0
    while (is_wifi_connected is not True) and (compteur < 5):
        is_wifi_connected = test_wifi()
        compteur += 1
        if is_wifi_connected is not True:
            time.sleep(10)

    compteur = 0

    print(is_conf_file_here,"fichier")
    print(is_wifi_connected,"internet")

    if is_wifi_connected and is_conf_file_here:
        return True
    else:
        return False
