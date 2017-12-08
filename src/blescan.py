from bluepy.btle import Scanner, DefaultDelegate

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


def mac_filter(global_list,sensors_mac_list): #compare les MAC des appareils bluetooth scannés avec les MAC des capteurs

    alert_list_return = []                   #purge de la liste d'alerte en entrée de fonction
    for scanned_mac in global_list:             #compare chaque élement de global_list
        for sensor_mac in sensors_mac_list:         #à chaque élément de sensors_mac_list
            is_a_sensor = (scanned_mac == sensor_mac)
            if is_a_sensor:
                alert_list_return.append(scanned_mac)

    return alert_list_return

#debug test
sensors_mac_list = ["3a:56:d7:b3:7f:d1", "f2:bb:dc:d3:16:85", "09:00:c5:34:28:66", "0b:11:fa:07:e4:c2","18:ed:a2:8f:5c:b2","1e:a6:60:c5:dc:49","54:60:09:db:35:25","0f:33:30:52:dc:19"]
alert_list = mac_filter(bluetooth_scan(),sensors_mac_list)
print(bluetooth_scan())
print(alert_list)
