#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates

# utilitaire pour ouvrir un file destinataires
dest = open('destinataires', 'r')
destinataires = dest.read()
destinataires = destinataires.split("\n")
d1 = ', '.join(destinataires)

# utilitaire pour écrire dans un file historique
histo = open('historique', 'a')
# utilitaire de gestion des dates
date = datetime.datetime.now()
histo.write("\nUn email a été envoyé à:\n" + d1 + str(date) + "\n-------------------") # le \n pour un saut de ligne
histo.close()
