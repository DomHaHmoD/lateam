#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime # import pour gérer les dates

# utilitaire de gestion des capteurs
capteurs = open('capteurs', 'w')
#capteurs = capt.read()
#capteurs = capteurs.split("\n")
date = datetime.datetime.now()
capteurs.write("""['00:1A:2B:3C:5E','cafetière'],
['00:4A:3B:3C:4B','ferrari'],
['00:5A:0B:8C:3C','sardine']]""")
capteurs.close()
