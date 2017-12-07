#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
import datetime # import pour gérer les dates
import objet_sensor
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dest1 = "maxime.girma@hotmail.fr"
dest2 = "kev_wfc@hotmail.fr"

with open('destinataires.csv', newline = '') as file:
    listdestinataires = csv.reader(file)
    #print('passage1',file)
    for row in listdestinataires:
        print(row) #print la ligne entiere avec les accolades
        print(row[0], row[1]) # print chaque élément
        print("----------------------")
        if row[1] == dest1 or row[1] == dest2:
            print("gagné")
            destinatairenotify = row[1]
        else:
            print("perdu")

#titi = objet_sensor.name
titi = objet_sensor.list_sensors_export()
print("ceci est titi:",titi)

#tutu = time
date = datetime.datetime.now()

msg = MIMEMultipart()
msg['From'] = 'secure.stand2017@gmail.com'
msg['To'] = destinatairenotify
msg['Subject'] = 'Alerte sur votre stand'
message = """Bonjour !
le capteur de votre stand positionné sur {}
à {}

le systeme SecureStand
DHI""".format(titi, date)
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('secure.Stand2017@gmail.com', 'pythonlinux')
mailserver.sendmail('secure.Stand2017@gmail.com', destinatairenotify, msg.as_string())
mailserver.quit()

# appelle d'une fonction dans un file externe
# exec(open('writehistoric.py').read())

