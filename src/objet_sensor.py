
import time
#creation d'une class
class Sensor:
	def __init__(self,mac,name):
		self.mac = mac
		self.name = name
		self.last_alert = time.time()


sensors_list =[]


sensors_list.append(Sensor("23:2a:35","cafetiere"))
sensors_list.append(Sensor("13:2a:35","voiture"))
sensors_list.append(Sensor("23:2a:b5","tabouret"))
sensors_list.append(Sensor("23:2a:c5","table"))
sensors_list.append(Sensor("00:2a:35","raspberry"))
a=sensors_list[0].last_alert

for kabla in sensors_list:
	print(kabla.name, kabla.mac)
time.sleep(5)
sensors_list[0].last_alert = time.time()
sensors_list[1].name = "pouet"
print(sensors_list[1].name)
print(sensors_list[0].last_alert - a)

#Sensor_1 = Sensor("28:31:25","cafetière")
#Sensor_2 = Sensor("29:31:25","voiture")
#Sensor_3 = Sensor("30:31:25","tabouret")

#print(Sensor_1.name,Sensor_1.mac)
#time.sleep(5)
#print(time.time()-Sensor_1.last_alert)
