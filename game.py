import os
import sys
from modules.combat import *
from modules.utilitaires import *
import random

a=1
while a==1:
	choix=menu_3_choix("MENU PRINCIPAL","Expédition","Aptitudes","Quartier marchand","Quitter")
	if str(choix)=="0":
		quit()
	elif str(choix)=="1":
		
	elif str(choix)=="2":
		b=1
		while b==1:
			choix=menu_3_choix("APTITUDES","Spécialisation","Maîtrise","Transcendance","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_3_choix("SPECIALISATION","Puissance","Resistance","Agilité","Retour")
				#
			elif str(choix)=="2":
				choix=menu_3_choix("MAITRISE","Elémentaires","Vengeresse","","Retour")
			elif str(choix)=="3":
				choix=menu_3_choix("TRANSCENDANCE","","","","Retour")
			else:
				pass
	elif str(choix)=="3":
		b=1
		while b==1:
			choix=menu_3_choix("QUARTIER MARCHAND","Marché noir","Hôtel des ventes","Joaillerie","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_3_choix("MARCHE NOIR","Adrenaline","Pioche de Stakhanov","Potion d'invisibilité","Retour")
			elif str(choix)=="2":
				choix=menu_3_choix("HOTEL DES VENTES","Acheter des pierres","Vendre des pierres","Investir","Retour")
			elif str(choix)=="3":
				choix=menu_3_choix("JOAILLERIE","Fabriquer","Polir","Investir","Retour")
			else:
				pass
	else:
		pass
    
