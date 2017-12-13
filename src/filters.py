import time

def mac_filter(global_list,sensors_list): #compare les MAC des appareils bluetooth scannés avec les MAC des capteurs

    alert_list_return = []                   #purge de la liste d'alerte en entrée de fonction
    for scanned_mac in global_list:             #compare chaque élement de global_list
        for sensor in sensors_list:
            sensor_mac = sensor.mac
            is_a_sensor = (scanned_mac == sensor_mac)
            if is_a_sensor:
                alert_list_return.append(sensor)

    return alert_list_return


def time_filter(alert_list):

    final_alert_list_return = []

    for item in alert_list:         # on itère sur chaque objet de alert_list

        if (time.time() - item.last_alert) > 60:  # si la dernière alerte est plus ancienne que 60 sec

            final_alert_list_return.append(item)  # on ajoute l'objet dans la liste finale

    return final_alert_list_return
