import os
import sys
from modules.combat import *
from modules.utilitaires import *
import random

a=1
while a==1:
	choix=menu_x_choix("MENU PRINCIPAL","Expédition","Aptitudes","Quartier marchand","Quitter")
	if str(choix)=="0":
		quit()
	elif str(choix)=="1":
		print ("En cours de dev")
	elif str(choix)=="2":
		b=1
		while b==1:
			choix=menu_x_choix("APTITUDES","Apprendre","Consulter","Réinitialiser","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_x_choix("APPRENDRE","Vivacité","Puissance","Résistance","Retour")
			elif str(choix)=="2":
				c=1
				while c==1:
					choix=menu_x_choix("CONSULTER","Traits","Spécialisations","Maîtrises","Retour")
					if str(choix)=="0":
						c=0
						pass
					elif str(choix)=="1":
						choix=menu_x_choix("TRAITS","Vivacité","Puissance","Résistance","Retour")
						if str(choix)=="0":
							pass
						elif str(choix)=="1":
							consult("VIVACITE","+5% chance rejouer","+5% force <-> +5% vitesse","+5% chance rejouer","+7% précision <-> +7% technique","Quand vous rejouez, +10% vitesse <-> +10% force","+6% force <-> +6% vitesse <-> +3% force et vitesse","+15% chance rejouer mais palier 5 désactivé <-> -5% chance rejouer mais palier 5 s'applique sur la force et la vitesse","+9% précision <-> +9% technique <-> +4% précision et technique","+1 point d'énergie")
						elif str(choix)=="2":
							consult("PUISSANCE","+10% chance critique","+5% force <-> +5% vie","+10% chance critique","+14% brutalité <-> +7% technique","+10% chance critique <-> lors d'un critique, ignore 30% armure","+6% force <-> + 6% vie <-> +3% force et vie","-40% force +20% chance critique +25% brutalité <-> les critiques ignorent 60% de l'armure","+18% brutalité <-> +9% technique <-> +9% brutalité et +4% technique","+1 point d'énergie")
						elif str(choix)=="3":
							consult("RESISTANCE")
						else:
							pass
					elif str(choix)=="2":
						choix=menu_x_choix("SPECIALISATIONS","Insaisissable","Elémentaire","Sanguinaire","Retour")
						if str(choix)=="0":
							pass
						elif str(choix)=="1":
							consult("INSAISISSABLE")
						elif str(choix)=="2":
							consult("ELEMENTAIRE")
						elif str(choix)=="3":
							consult("SANGUINAIRE")
						else:
							pass
					elif str(choix)=="3":
						choix=menu_x_choix("MAITRISES","Surpuissance","Transcendance","Perseverance","Fulgurance","Prédominance","Arrogance","Flamboyance","Clairvoyance","Souffrance","Retour")
						if str(choix)=="0":
							pass
						elif str(choix)=="1":
							consult("SURPUISSANCE")
						elif str(choix)=="2":
							consult("TRANSCENDANCE")
						elif str(choix)=="3":
							consult("PERSEVERANCE")
						elif str(choix)=="4":
							consult("FULGURANCE")
						elif str(choix)=="5":
							consult("PREDOMINANCE")
						elif str(choix)=="6":
							consult("ARROGANCE")
						elif str(choix)=="7":
							consult("FLAMBOYANCE")
						elif str(choix)=="8":
							consult("CLAIRVOYANCE")
						elif str(choix)=="9":
							consult("SOUFFRANCE")
			elif str(choix)=="3":
				print ("En cours de dev")
			else:
				pass
	elif str(choix)=="3":
		b=1
		while b==1:
			choix=menu_x_choix("QUARTIER MARCHAND","Marché noir","Hôtel des ventes","Joaillerie","Retour")
			if str(choix)=="0":
				b=0
				pass
			elif str(choix)=="1":
				choix=menu_x_choix("MARCHE NOIR","Adrenaline","Pioche de Stakhanov","Potion d'invisibilité","Retour")
			elif str(choix)=="2":
				choix=menu_x_choix("HOTEL DES VENTES","Acheter des pierres","Vendre des pierres","Investir","Retour")
			elif str(choix)=="3":
				choix=menu_x_choix("JOAILLERIE","Fabriquer","Polir","Investir","Retour")
			else:
				pass
	else:
		pass
    
