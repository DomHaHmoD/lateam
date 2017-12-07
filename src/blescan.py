# TODO fonction a decouper en 2 (scan et filtre)



def bluetooth_scan():

    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)

        def handleDiscovery(self, dev, isNewDev, isNewData):
            if isNewDev:
                print ("Discovered device", dev.addr)
            elif isNewData:
                print ("Received new data from", dev.addr)

    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)
    global_list = []
    #injecte les adresse Mac de tous les appareils dans une global_list
    for dev in devices:
        global_list.append(dev.addr)

    return global_list


def mac_filter(global_list,sensors_list):

    alert_list_return = []                   #purge de la liste d'alerte en entrée de fonction
    for scanned_mac in global_list:
        for sensor_mac in sensors_list:
            is_a_sensor = (scanned_mac == sensor_mac)   #booléen
            print(is_a_sensor) #debug test

            if is_a_sensor:
                alert_list_return.append(scanned_mac)

    return alert_list_return


sensors_list = ["0b:11:fa:07:e4:c2","18:ed:a2:8f:5c:b2","1e:a6:60:c5:dc:49","54:60:09:db:35:25","0f:33:30:52:dc:19"] #debug test liste fictive
alert_list = mac_filter(bluetooth_scan(),sensors_list)
print(alert_list)


#def filtreTemps(listeAlerte):
#    import time
#    import datetime
#    date = datetime.now()
#    return date
