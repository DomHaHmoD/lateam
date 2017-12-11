import time

def update_sensors_list(sensors_list,final_alert_list):

    for item in sensors_list:

        i = 0
        while i < len(final_alert_list):
            if item.name == final_alert_list[i].name:
                item.last_alert = time.time()
                print  ("MISE A JOUR !",item.last_alert)

                i += 1

    return sensors_list
