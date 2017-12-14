#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
DominiqueHathi
11/12/2017
version 0.9

La fonction prend en argument la liste des destinataires, des alertes et des alertes en attente.
Elle envoie une alerte correspondant aux listes aux destinataires.
Elle renvoie au MAIN un False en cas d'erreur.
'''

#import time
import datetime # import pour gérer les dates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def notify(recipients_list, final_alert_list):

    name_list = []

    for item in final_alert_list:  # on crée une liste de noms à partir de chaque objet
        name_list.append(item.name)

    #date
    date = datetime.datetime.now()

    #gestion du mail
    msg = MIMEMultipart()
    msg['From'] = 'secure.stand2017@gmail.com'
    msg['To'] = ','.join(recipients_list)
    msg['Subject'] = 'Alerte sur votre stand'
    message = """Bonjour,
    le (les) capteur(s) de votre stand positionné(s) sur le(la) {}
    s'est déclenché
    à {}

    Cordialement,
    Le systeme SecureStand
    """.format(name_list, date)
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('secure.Stand2017@gmail.com', 'pythonlinux')
    mailserver.sendmail('secure.Stand2017@gmail.com', recipients_list, msg.as_string())
    print("mail envoyé")
    mailserver.quit()

    return True
