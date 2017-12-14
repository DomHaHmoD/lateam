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

name_list = []

#date
date = datetime.datetime.now()

def format_welcome_mail(date):
    #partie entete de mail pour le démarrage
    subject = 'SecureStand vous souhaite le bienvenue'

    # partie corps de message pour le démarrage
    content = """Bonjour,
    votre système SecureStand a bien démarré
    à {}
    Cordialement,
    Le systeme SecureStand
    """.format(date)
    return subject, content

def format_alert_mail(name_list, date):
     #partie entete de mail pour les alertes
    subject = 'Alerte sur votre stand'

    # partie corps de message pour les alertes
    content = """Bonjour,
    le (les) capteur(s) de votre stand positionné(s) sur le(la) {}
    s'est déclenché
    à {}

    Cordialement,
    Le systeme SecureStand
    """.format(name_list, date)
    return subject, content


def notify(recipients_list, final_alert_list):

    # partie entete de mal commune
    msg = MIMEMultipart()
    msg['From'] = 'secure.stand2017@gmail.com'
    msg['To'] = ','.join(recipients_list)
    print(final_alert_list)
    if len(final_alert_list) == 0:
        subject, content = format_welcome_mail(date)
        print(subject, content)
    else:
        for item in final_alert_list:  # on crée une liste de noms à partir de chaque objet
            name_list.append(item.name)

        #gestion du mail
        subject, content = format_alert_mail(name_list, date)

        #msg.attach(MIMEText(message))

    msg['Subject'] = subject
    msg.attach(MIMEText(content))
    # partie gestion de mail
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('secure.Stand2017@gmail.com', 'pythonlinux')
    mailserver.sendmail('secure.Stand2017@gmail.com', recipients_list, msg.as_string())
    print("mail envoyé")
    mailserver.quit()

    return True

