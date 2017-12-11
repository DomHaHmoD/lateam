
def get_alert_frequence_data():
    alert_frequence = 0

    try:
        with open('alert_frequence.csv') as file: # ouverture du csv
            temporary = list(csv.reader(file))# les 3 lignes suivantes servent à recuperer un int en le sortant
            temporary2 = temporary[0]#          par à coup de la double liste
    except FileNotFoundError:
        alert_frequence = 60
        print("NO ALERT_FREQUENCE.CSV")
        return alert_frequence

    try:
        alert_frequence = int(temporary2[0])
    except ValueError:
        alert_frequence = 60
    print(alert_frequence,"est la frequence d'alerte")#print de test
    return alert_frequence
