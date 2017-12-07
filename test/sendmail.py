#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# utilitaire pour ouvrir un file destinataires
dest = open('destinataires', 'r')
destinataires = dest.read()
destinataires = destinataires.split("\n")


msg = MIMEMultipart()
msg['From'] = 'dominique.hathi@gmail.com'
msg['To'] = 'dominique.hathi@gmail.com'
msg['Subject'] = 'Le sujet de mon mail' 
message = """Bonjour !
le capteur N° 5 de votre stand positionné sur la cafetière
à 16h00

le systeme SecureStand
DHI"""
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('secure.Stand2017@gmail.com', 'pythonlinux')
mailserver.sendmail('secure.Stand2017@gmail.com', destinataires, msg.as_string())
mailserver.quit()

execfile('writehistoric.py')


