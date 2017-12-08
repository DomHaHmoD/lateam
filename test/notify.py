#!/usr/bin/env python
#-*- coding: utf-8 -*-


import datetime # import pour gérer les dates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recipients_list = ["dominique.hathi@gmail.com","maxime.girma@hotmail.fr","kev_wfc@hotmail.fr","raoultson@yahoo.fr"]

alerte_list = ["ferrari"]


def notify(recipients_list, alerte_list):

    #objet qui bouge
    objet = alerte_list
    print("ceci est objet:",objet)

    #date
    date = datetime.datetime.now()

    COMMASPACE = ','

    msg = MIMEMultipart()
    msg['From'] = 'secure.stand2017@gmail.com'
    msg['To'] = COMMASPACE.join(recipients_list)
    msg['Subject'] = 'Alerte sur votre stand'
    message = """Bonjour,
    le capteur de votre stand positionné sur le(la) {}
    s'est déclanché
    à {}
    
    Cordialement,
    Le systeme SecureStand
    """.format(objet, date)
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('secure.Stand2017@gmail.com', 'pythonlinux')
    mailserver.sendmail('secure.Stand2017@gmail.com', recipients_list, msg.as_string())
    print("mail envoyé")
    mailserver.quit()

    # appelle d'une fonction dans un file externe
    #exec(open('writehistoric.py').read())


notify(recipients_list,alerte_list)

