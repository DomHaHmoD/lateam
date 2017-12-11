#!/usr/bin/env python
#-*- coding: utf-8 -*-


import datetime # import pour gérer les dates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#recipients_list = ["dominique.hathi@gmail.com","maxime.girma@hotmail.fr","kev_wfc@hotmail.fr","raoultson@yahoo.fr"]
#recipients_list = ["dominique.hathi@gmail.com"]
#alerte_list = ['ferrari', 'tabouret']
#alerte_list = ['ferrari']

def notify(recipients_list, alert_list,alert_frequence):

    name_list = []
    for alert in alert_list:
        if alert.last_alert < alert_frequence :
            name_list.append(alert.name)

    COMMASPACE = ','

    #objet qui bouge
    objetquibouge = list(name_list)
    """if len(objetquibouge) > 1:
        print("ceci est objet 1:",objetquibouge)
        ', '.join(objetquibouge)
        print("ceci est objet:",objetquibouge)
    else:
        ', '.join(objetquibouge)"""

    #date
    date = datetime.datetime.now()

    #gestion du mail
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
    """.format(objetquibouge, date)
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
