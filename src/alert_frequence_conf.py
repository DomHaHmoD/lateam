
def get_alert_frequence_data():
    alert_frequence = 0
    with open('alert_frequence.csv') as file: # ouverture du csv
        temporary = list(csv.reader(file))# les 3 lignes suivantes servent à recuperer un int en le sortant
        temporary2 = temporary[0]#          par à coup de la double liste
        try:
            alert_frequence = int(temporary2[0])
        except ValueError:
            alert_frequence = 60
    return alert_frequence