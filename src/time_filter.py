import time

def time_filter(alert_list):

    final_alert_list_return = []

    for item in alert_list:         # on itère sur chaque objet de alert_list

        if (time.time() - item.last_alert) > 60:  # si la dernière alerte est plus ancienne que 60 sec

            final_alert_list_return.append(item)  # on ajoute l'objet dans la liste finale

    return final_alert_list_return
