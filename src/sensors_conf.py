'''
KevinGeorget
12/12/2017
version 0.9

get_sensors_data() definit une classe d'objet "sensor" puis ouvre un fichier CSV
Elle construit ensuite une liste d'objets basées sur les caractèristiques du fichier CSV.
Elle renvoie ensuite cette liste au MAIN.
'''
import csv


# definition de la class capteur


class Sensor:

    def __init__(self, mac, name):
        self.mac = mac
        self.name = name
        self.last_alert = 0


def get_sensors_data():

    sensors_list_return = []   # création de la liste d'objets "sensors"

    with open('sensors_conf.csv') as file:     # ouverture du CSV config
        sensors_conf = csv.reader(file, delimiter=',')
        file.readline()     # on consomme la 1ere ligne (entrée tableau)

        for row in sensors_conf:
            if row[1] == "":
                sensors_list_return.append(Sensor(row[0], "Aucun objet associé"))  # création/insertion des objets dans
                # la liste
            else:
                sensors_list_return.append(Sensor(row[0], row[1]))

    return sensors_list_return

# TESTS


sensors_list = get_sensors_data()

print(sensors_list[0].mac, sensors_list[1].mac, sensors_list[2].mac, sensors_list[3].mac, sensors_list[4].mac, sensors_list[5].mac, sensors_list[6].mac, sensors_list[7].mac)
print(sensors_list[0].name, sensors_list[1].name, sensors_list[2].name, sensors_list[3].name, sensors_list[4].name, sensors_list[5].name, sensors_list[6].name, sensors_list[7].name)

"""name_list = sensors_conf[0]  # on sépare les données dans 2 listes distinctes
mac_list = sensors_conf[1]
name_list = name_list[1:]  #on tronque les entrées du tableau
mac_list = mac_list[1:]





index = 0 #indice des listes de noms et d'adresses MAC
while(index < len(mac_list) or index < len(name_list)):  #on s'arrete si il manque une donnée dans la config
    sensors_list_return.append(Sensor(mac_list[index], name_list[index]))
# on créé des objets qui portent le nom des objets du stand, et qui ont pour propriétés
# l'adresse mac et le nom de l'objet du stand (ex Ferrari: mac: "A1:F0:..." nom: "ferrari")
    index += 1"""
