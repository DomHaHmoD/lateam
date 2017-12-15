'''
KevinGeorget
13/12/2017
Version 1.0

La fonction bluetooth_scan utilise la librairie BluePy pour scanner tous les appareils bluetooth
proches. La fonction récupère les adresses MAC de ces appareils et les stocke dans une liste (global_list)
Cette liste d'adresse MAC est ensuite renvoyée à la fonction MAIN.
'''


from bluepy.btle import Scanner


def bluetooth_scan():

    print("coucou je rentre dedans")  # debug test

    devices = Scanner().scan(10.0)
    global_list = []
    # injecte les adresse Mac de tous les appareils dans une global_list
    for dev in devices:
        global_list.append(dev.addr)

    return global_list


"""def mac_filter(global_list,sensors_list): #compare les MAC des appareils bluetooth scannés avec les MAC des capteurs

    alert_list_return = []                   #purge de la liste d'alerte en entrée de fonction
    for scanned_mac in global_list:             #compare chaque élement de global_list
        for sensor in sensors_list:
            sensor_mac = sensor.mac
            is_a_sensor = (scanned_mac == sensor_mac)
            if is_a_sensor:
                alert_list_return.append(sensor)

    return alert_list_return

#debug test
class Sensor:

	def __init__(self,mac,name):
		self.mac = mac
		self.name = name
		self.last_alert = 0

sensors_list=[]
sensors_list.append(Sensor("3b:f5:5e:c4:3e:9c","ferrari"))
sensors_list.append(Sensor("0b:9e:09:d6:14:d4","trompette"))
sensors_list.append(Sensor("2e:66:aa:04:9c:ec","paté"))
sensors_list.append(Sensor("3b:87:f9:93:c9:f5","chaise"))
sensors_list.append(Sensor("07:39:8a:d0:7b:36","truite"))

global_list = bluetooth_scan()

alert_list = mac_filter(global_list, sensors_list)

for alert in alert_list:
    print(alert.mac, alert.name)"""
