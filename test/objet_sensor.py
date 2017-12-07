#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
#creation d'une class

class Sensor:
	def __init__(self,mac,name):
		self.mac = mac
		self.name = name
		self.last_alert = time.time()

export_name = []

def list_sensors_export():
	sensors_list =[]

	sensors_list.append(Sensor("23:2a:35","cafetiere"))
	sensors_list.append(Sensor("13:2a:35","voiture"))
	sensors_list.append(Sensor("23:2a:b5","tabouret"))
	sensors_list.append(Sensor("23:2a:c5","table"))
	sensors_list.append(Sensor("00:2a:35","raspberry"))
	a=sensors_list[0].last_alert


	for kabla in sensors_list:
		if kabla.mac == "13:2a:35":
			print("gagné",kabla.name)
			export_name.append(kabla.name)
		else:
			print("perdu",kabla.name)

	return export_name

#time.sleep(5)
#sensors_list[0].last_alert = time.time()
#sensors_list[1].name = "pouet"
#print(sensors_list[1].name)
#print(sensors_list[0].last_alert - a)

