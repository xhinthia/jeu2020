import os
import sys
from modules.combat import *
from modules.utilitaires import *
import random


if os.path.isfile("traits.txt")=="false":
	trait=0
	trait_p1=0
	trait_p2=0
	trait_p3=0
	trait_p4=0
	trait_p5=0
	trait_p6=0
	trait_p7=0
	trait_p8=0
	trait_p9=0
	fw = open("traits.txt","w")
	fw.write(str(trait))
	fw.write("\n")
	fw.write(str(trait_p1))
	fw.write("\n")
	fw.write(str(trait_p2))
	fw.write("\n")
	fw.write(str(trait_p3))
	fw.write("\n")
	fw.write(str(trait_p4))
	fw.write("\n")
	fw.write(str(trait_p5))
	fw.write("\n")
	fw.write(str(trait_p6))
	fw.write("\n")
	fw.write(str(trait_p7))
	fw.write("\n")
	fw.write(str(trait_p8))
	fw.write("\n")
	fw.write(str(trait_p9))
	fw.close()
if os.path.isfile("specialisations.txt")=="false":
	specialisation=0
	specialisation_p1=0
	specialisation_p2=0
	specialisation_p3=0
	specialisation_p4=0
	specialisation_p5=0
	specialisation_p6=0
	specialisation_p7=0
	specialisation_p8=0
	specialisation_p9=0
	fw = open("traits.txt","w")
	fw.write(str(specialisation))
	fw.write("\n")
	fw.write(str(specialisation_p1))
	fw.write("\n")
	fw.write(str(specialisation_p2))
	fw.write("\n")
	fw.write(str(specialisation_p3))
	fw.write("\n")
	fw.write(str(specialisation_p4))
	fw.write("\n")
	fw.write(str(specialisation_p5))
	fw.write("\n")
	fw.write(str(specialisation_p6))
	fw.write("\n")
	fw.write(str(specialisation_p7))
	fw.write("\n")
	fw.write(str(specialisation_p8))
	fw.write("\n")
	fw.write(str(specialisation_p9))
	fw.close()
	"""
if os.path.isfile("maitrises.txt")=="false":
	fw = open("sauv.txt","w")
	fw.write(str(nom))
	fw.write("\n")
	fw.write(str(lvl))
	fw.write("\n")
	"""


a=1
while a==1:
	choix=menu_x_choix(1,"MENU PRINCIPAL","Expédition","Aptitudes","Quitter")
	if str(choix)=="4":
		quit()
	elif str(choix)=="1":
		
	elif str(choix)=="2":
		b=1
		while b==1:
			choix=menu_x_choix(1,"APTITUDES","Destin","Potentiel","Renouveau","Retour")
			if str(choix)=="4":
				b=0
				pass
			elif str(choix)=="1":
				"""if str(point_aptitude)=="0":
					print ("Vous avez 0 point d'aptitude... Revenez me voir plus tard.")
				else:
					if str(select_trait)=="1":
						if str(select_specialisation)=="1":
							if str(select_maitrise)=="1":
								if str(palier1_maitrise)=="1":"""
			elif str(choix)=="2":
				c=1
				while c==1:
					choix=menu_x_choix(1,"DESTIN","Traits","Spécialisations","Maîtrises","Retour")
					if str(choix)=="4":
						c=0
						pass
					elif str(choix)=="1":
						choix=menu_x_choix(1,"TRAITS","Vivacité","Puissance","Résistance","Retour")
						if str(choix)=="4":
							pass
						elif str(choix)=="1":
							consult(1,"VIVACITE","+5% chance rejouer","+5% force <-> +5% vitesse","+5% chance rejouer","+7% précision <-> +7% technique","Quand vous rejouez, +10% vitesse <-> +10% force","+6% force <-> +6% vitesse <-> +3% force et vitesse","+15% chance rejouer mais palier 5 désactivé <-> -5% chance rejouer mais palier 5 s'applique sur la force et la vitesse","+8% précision <-> +8% technique <-> +4% précision et technique","+1 point d'énergie","Débloque les spécialisations")
						elif str(choix)=="2":
							consult(1,"PUISSANCE","+10% chance critique","+5% force <-> +5% vie","+10% chance critique","+14% brutalité <-> +7% technique","+10% chance critique <-> lors d'un critique, ignore 30% armure","+6% force <-> + 6% vie <-> +3% force et vie","-40% force +20% chance critique +25% brutalité <-> les critiques ignorent 60% de l'armure","+18% brutalité <-> +8% technique <-> +8% brutalité et +4% technique","+1 point d'énergie","Débloque les spécialisations")
						elif str(choix)=="3":
							consult(1,"RESISTANCE","+7% blocage","+5% vie <-> +5% armure","+7% blocage","+7% ténacité <-> +7% technique","+15% blocage <-> Si blocage, inflige votre armure en dégat","+6% vie <-> +6% armure <-> +3% vie et armure","+20% blocage mais réduit la réduc dgt <-> -10% blocage mais augmente la réduc dgt","+8% ténacité <-> +8% technique <-> +4% ténacité et technique","+1 point d'énergie","Débloque les spécialisations")
						else:
							pass
					elif str(choix)=="2":
						choix=menu_x_choix(1,"SPECIALISATIONS","Insaisissable","Elémentaire","Sanguinaire","Retour")
						if str(choix)=="4":
							pass
						elif str(choix)=="1":
							consult(1,"INSAISISSABLE","+5% esquive","+5% vitesse <-> +5% armure","+7% précision <-> +7% brutalité","+7% ténacité <-> +7% technique","+5% esquive","+6% vitesse <-> +8% ténacité","+6% armure <-> +8% brutalité","+8% précision <-> +8% technique","Après une esquive, contre-attaque dispo (100% cc)","Débloque les maîtrises")
						elif str(choix)=="2":
							consult(1,"ELEMENTAIRE","+5% poser sceau","+5% force <-> +7% technique","+5% vitesse <-> +7% technique","+7% ténacité <-> +5% force","+5% poser sceau élementaire (feu,glace,foudre) max 3","+6% vitesse <-> +8% ténacité","+8% technique <-> +6% force","+6% vie <-> +6% armure","sort : instabilité élementaire qui consomme les sceaux","Débloque les maîtrises")
						elif str(choix)=="3":
							consult(1,"SANGUINAIRE","+5% chance de plaie","+5% force <-> +5% vie","+5% vie <-> +7% précision","+5% force <-> +7% brutalité","+5% chance de plaie (cc inflige 2 plaies)","+6% force <-> +6% vitesse","+6% vie <-> +6% force","+8% précision <-> +8% brutalité","sort torture : inflige autant de plaie que tes points d'énergie et perd 1 point pour le reste du combat","Débloque les maîtrises")
						else:
							pass
					elif str(choix)=="3":
						choix=menu_x_choix(1,"MAITRISES","Surpuissance","Transcendance","Perseverance","Fulgurance","Prédominance","Arrogance","Flamboyance","Clairvoyance","Souffrance","Retour")
						if str(choix)=="4":
							pass
						elif str(choix)=="1":
							consult(1,"SURPUISSANCE")
						elif str(choix)=="2":
							consult(1,"TRANSCENDANCE")
						elif str(choix)=="3":
							consult(1,"PERSEVERANCE")
						elif str(choix)=="4":
							consult(1,"FULGURANCE")
						elif str(choix)=="5":
							consult(1,"PREDOMINANCE")
						elif str(choix)=="6":
							consult(1,"ARROGANCE")
						elif str(choix)=="7":
							consult(1,"FLAMBOYANCE")
						elif str(choix)=="8":
							consult(1,"CLAIRVOYANCE")
						elif str(choix)=="9":
							consult(1,"SOUFFRANCE")
	else:
		pass
    
