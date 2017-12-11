def update_sensors_list(sensors_list,alert_list):

    i = 0

    for item in sensors_list:
        while i < len(alert_list):

            if item.name == alert_list[i].name:
                item.last_alert = time.time()
                print  ("MISE A JOUR !",item.last_alert)
            i += 1
    
    return sensors_list
