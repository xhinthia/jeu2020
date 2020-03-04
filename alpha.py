import os
import os.path
import sys
import random
from modules.utilitaires import *
import time

point_aptitude=18
vie=1000
force=325
arm=150
vit=100
preci=1
brut=50
touch=1
tech=1

if os.path.isfile("trait_selection.txt")=="false":
	fw = open("trait_selection.txt","w")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))
	fw.close()
if os.path.isfile("trait_global_vivacite.txt")=="false":
	fw = open("trait_global.txt","w")
	fw.write(str("VIVACITE"))
	fw.write("\n")
	fw.write(str("Frappe rapide à une chance de vous rendre 1 point d'énergie (1% + technique)"))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str("Les dégats successifs dans un même tour augmente (+10% à chaque itération)"))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str("1 point d'énergie en plus"))
	fw.close()
"""
else:
	liste_trait = []
	with open("trait.txt","r") as f_read:
		for line in f_read:
			line=line.strip()
			liste_trait.append(line)
	f_read.close()
	trait0 = liste_trait[0]
	trait1 = liste_trait[1]
	trait2 = liste_trait[2]
	trait3 = liste_trait[3]
	trait4 = liste_trait[4]
	trait5 = liste_trait[5]
	trait6 = liste_trait[6]
	trait7 = liste_trait[7]
	trait8 = liste_trait[8]
	trait9 = liste_trait[9]
if os.path.isfile("specialisations.txt")=="false":
	specialisation0=0
	specialisation1=0
	specialisation2=0
	specialisation3=0
	specialisation4=0
	specialisation5=0
	specialisation6=0
	specialisation7=0
	specialisation8=0
	specialisation9=0
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
else:
	liste_specialisation = []
	with open("trait.txt","r") as f_read:
		for line in f_read:
			line=line.strip()
			liste_specialisation.append(line)
	f_read.close()
	specialisation0 = liste_specialisation[0]
	specialisation1 = liste_specialisation[1]
	specialisation2 = liste_specialisation[2]
	specialisation3 = liste_specialisation[3]
	specialisation4 = liste_specialisation[4]
	specialisation5 = liste_specialisation[5]
	specialisation6 = liste_specialisation[6]
	specialisation7 = liste_specialisation[7]
	specialisation8 = liste_specialisation[8]
	specialisation9 = liste_specialisation[9]
"""
choix=input("Voulez-vous passer les explications ? [1 - Non] [2 - Oui] : ")
if str(choix)=="1":
	print ("Bienvenue dans l'alpha de XZ GAME !")
	time.sleep(0.7)
	print ("")
	print ("Cet alpha a pour but de découvrir les possibilités de build qu'offre l'arbre de talent et de découvrir la mécanique des combats")
	print ("")
	time.sleep(0.7)
	print ("Dans le menu prncipal, vous aurez le choix entre :")
	print ("")
	time.sleep(0.5)
	print ("l'expédition, qui commence directement un nouveau combat contre un poutch avec énormément de vie et réalisant la même attaque à chaque tour.")
	time.sleep(0.5)
	print ("rien de très excitant mais il vous permet de tester vos build, autant les build dps que les build de défense")
	time.sleep(0.5)
	print ("vous pourrez quitter à tout moment le combat en utilisant 'quitter' pour tester d'autre chose")
	time.sleep(0.5)
	print ("")
	print ("les traits qui représentent la première possibilité d'augmentation type 'arbre de talent' proposé dans le jeu")
	time.sleep(0.5)
	print ("vous avez 3 choix, vous pouvez consulter l'ensemble des améliorations proposées par chacun d'entre eux dans la partie 'consultation'")
	time.sleep(0.5)
	print ("")
	print ("Enfin, les spécialisations qui sont les deuxièmes arbres de talent disponibles")
	time.sleep(0.5)
	print ("Comme son prédécesseur, vous pouvez utiliser la partie 'consultation' pour avoir une vue globale des propositions offertes par chaque branche")
	time.sleep(1)
	print ("")
	input("Quand vous souhaitez continuer, appuyer sur n'importe quelle touche.")
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("Rapides explications sur les caractéristiques :")
	time.sleep(0.5)
	print ("- vie : rien d'original, si vous perdez votre vie... Vous perdez la vie quoi logique.")
	time.sleep(0.5)
	print ("- force : au plus tu en as, au plus tu tapes.")
	time.sleep(0.5)
	print ("- armure : réduit les dégats subis")
	time.sleep(0.5)
	print ("- vitesse : au plus tu as de vitesse au plus tu joues 'vite'")
	time.sleep(1)
	print ("")
	print ("Ce sont les 4 caractéristiques principales, jusque là j'ai rien révolutionné...")
	print ("Par contre la suite :)")
	time.sleep(1)
	print ("")
	print ("- la technique : de 0% à 100%, représente ta chance de lancer un sort en faisant une action")
	time.sleep(0.5)
	print ("- la précision : de 0% à 100% représente tes chances de faire un coup critique")
	time.sleep(0.5)
	print ("- la brutalité : augmente tes dégats critiques")
	time.sleep(0.5)
	print ("- le toucher : augmente tes chances de... toucher ta cible !")
	time.sleep(1)
	print ("")
	print ("Petit explication concernant la technique, j'en profite pour passer à l'explication sur les mécanismes de combat")
	print ("")
	input("Quand tu es prêt, appuie sur une touche")
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("en fonction de votre vitesse, soit tu commences soit c'est l'ennemi")
	time.sleep(0.5)
	print ("un bandeau informatif situé en haut d'écran vous donne toutes les informations utiles lors des combats")
	time.sleep(0.5)
	print ("Lorsque c'est à votre tour de jouer, vous avez 3 choix possibles (puis 4 grâce aux spécialisations) :")
	time.sleep(0.5)
	print ("- frappe rapide = inflige des dégats")
	time.sleep(0.5)
	print ("- frappe lourde = inflige des dégats")
	time.sleep(0.5)
	print ("- bouclier = augmente votre armure pour 1 tour")
	time.sleep(1)
	print ("")
	print ("Vous disposez de 3 points d'énergie (puis plus avec les talents et autre) pour effectuer des actions.")
	time.sleep(0.5)
	print ("chacune des 3 actions ci-dessus coûtent 1 point d'énergie")
	time.sleep(0.5)
	print ("chaque action a une chance (fonction de votre technique) de déclencher un sort")
	time.sleep(0.5)
	print ("Pour les besoins du test de cet alpha, vous n'avez pas la main sur les sorts exécutables")
	time.sleep(0.5)
	print ("De plus, la technique permet d'activer certains talents débloqués dans les traits et/ou les spécialisations très puissants")
	time.sleep(1)
	print ("Je pense que vous avez les bases")
	input("Pour commencer (enfin) à jouer, appuyez sur une touche")
	os.system('cls' if os.name == 'nt' else 'clear')
elif str(choix)=="2":
	a=1
	while a==1:
		choix=menu_x_choix(1,"MENU PRINCIPAL","Expéditions","Traits","Spécialisations","Quitter")
		if str(choix)=="4":
			quit()
		elif str(choix)=="1":
			print ("en cours de dev")
		elif str(choix)=="2":
			b=1
			while b==1:
				choix=menu_x_choix(1,"TRAITS","Choisir","Consulter","Réinitialiser","Retour")
				if str(choix)=="4":
					b=0
					pass
				elif str(choix)=="1":
					if point_aptitude>0:
						if str(trait0)=="0":
							bis=1
							while bis==1:
								choix=menu_x_choix(1,"TRAITS","Vivacité","Puissance","Résistance","Retour")
								if str(choix)=="4":
									bis=0
									pass
								elif str(choix)=="1":
									trait0="Vivacité"
									bis=0
								elif str(choix)=="2":
									trait0="Puissance"
									bis=0
								elif str(choix)=="3":
									trait0="Résistance"
									bis=0
					else:
						print ("Vous n'avez pas de points à dépenser")
						pass
				elif str(choix)=="2":
					print ("en cours de dev")
				elif str(choix)=="3":
					print ("en cours de dev")
		elif str(choix)=="3":
			b=1
			while b==1:
				choix=menu_x_choix(1,"SPECIALISATIONS","Choisir","Consulter","Réinitialiser","Retour")
				if str(choix)=="4":
					b=0
					pass
				elif str(choix)=="1":
					print ("en cours de dev")
				elif str(choix)=="2":
					c=1
					while c==1:
						choix=menu_x_choix(1,"CONSULTER","Insaisissable","Elementaire","Sanguinaire","Retour")
						if str(choix)=="4":
							c=0
							pass
						elif str(choix)=="1":
							print ("en cours de dev")
						elif str(choix)=="2":
							print ("en cours de dev")
						elif str(choix)=="3":
							print ("en cours de dev")
				elif str(choix)=="3":
					print ("en cours de dev")	
else:
	print ("Tu n'es pas foutu de taper 1 ou 2...? Ca promet pour la suite !")
	input()
	quit()
