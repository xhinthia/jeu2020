import os
import os.path
import sys
import random
from utilitaires import *
import time
from talent import *

if os.path.isfile("trait_selection.txt"):
	pass
else:
	fw = open("trait_selection.txt","w")
	fw.write(str(0))#I0
	fw.write("\n")
	fw.write(str(0))#P0
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P1
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P2
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P3
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P4
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P5
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P6
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P7
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P8
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P9
	fw.write("\n")
	fw.write(str(0))	
	fw.close()
if os.path.isfile("specialisation_selection.txt"):
	pass
else:
	fw = open("specialisation_selection.txt","w")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P0
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P1
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P2
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P3
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P4
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P5
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P6
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P7
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P8
	fw.write("\n")
	fw.write(str(0))
	fw.write("\n")
	fw.write(str(0))#P9
	fw.write("\n")
	fw.write(str(0))
	fw.close()
if os.path.isfile("trait_global_vivacite.txt")=="true":
	pass
else:
	fw = open("trait_global_vivacite.txt","w")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("VIVACITE"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Frappe rapide a une chance de vous rendre 1 point d'énergie (1% + technique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Les dégats successifs dans un même tour augmente (+10% à chaque itération)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de vitesse <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+1 point d'énergie"))
	fw.close()

if os.path.isfile("trait_global_puissance.txt")=="true":
	pass
else:
	fw = open("trait_global_puissance.txt","w")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("PUISSANCE"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Frappe lourde a une chance d'ignorer l'armure de la cible (2% + technique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +3% de précision <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +3% de précision <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +3% de précision <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Les coups critiques de frappe lourde ont une chance d'ignorer l'armure de la cible (15% + technique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +3% de précision <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +3% de précision <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +3% de précision <OU> +10% de brutalité"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+1 point d'énergie"))
	fw.close()

if os.path.isfile("trait_global_resistance.txt")=="true":
	pass
else:
	fw = open("trait_global_resistance.txt","w")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("RESISTANCE"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Bouclier a une chance de bloquer l'attaque (1% + technique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +7% de vie <OU> +6% d'armure"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +7% de vie <OU> +6% d'armure"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +7% de vie <OU> +6% d'armure"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Blocage inflige des dégats (50% de votre armure)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +7% de vie <OU> +6% d'armure"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +7% de vie <OU> +6% d'armure"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +7% de vie <OU> +6% d'armure"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+1 point d'énergie"))
	fw.close()

if os.path.isfile("specialisation_global_insaisissable.txt")=="true":
	pass
else:
	fw = open("specialisation_global_insaisissable.txt","w")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("INSAISISSABLE"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Vous avez une chance d'esquiver une attaque (1% + technique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de brutalité <OU> +6% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de brutalité <OU> +6% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de brutalité <OU> +6% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Lors d'une esquive, vous débloquez le 4e sort : Contre (100% de coup critique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de brutalité <OU> +6% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de brutalité <OU> +6% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de brutalité <OU> +6% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Votre vitesse augmente vos chances d'esquive (10% de votre vitesse)"))
	fw.close()

if os.path.isfile("specialisation_global_elementaire.txt")=="true":
	pass
else:
	fw = open("specialisation_global_elementaire.txt","w")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("ELEMENTAIRE"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Vous avez une chance de marquer la cible en infligeant des dégats (3 marques max): feu, foudre ou glace (1% + technique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +5% d'armure <OU> +4% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +5% d'armure <OU> +4% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +5% d'armure <OU> +4% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Débloque le 4e sort : Explosion élémentaire (lance un sort en fonction des éléments consommés)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +5% d'armure <OU> +4% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +5% d'armure <OU> +4% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +5% d'armure <OU> +4% de vitesse"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Vous avez une chance de conserver une marque élémentaire sur votre cible après les avoir consommées (30% de chance)"))
	fw.close()

if os.path.isfile("specialisation_global_sanguinaire.txt")=="true":
	pass
else:
	fw = open("specialisation_global_sanguinaire.txt","w")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("SANGUINAIRE"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Vous avez une chance de poser plaie sur la cible en infligeant des dégats (40% de chance)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +6% de vie <OU> +7% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +6% de vie <OU> +7% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +6% de vie <OU> +7% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Vous débloquez le 4e sort : Boucherie (consomme 10 plaies pour inflger 3 fois leurs dégats périodiques)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +6% de vie <OU> +7% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +6% de vie <OU> +7% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +6% de vie <OU> +7% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Les coups critiques posent 2 plaies sur la cible"))
	fw.close()

choix=input("Voulez-vous passer les explications ? [1 - Non] [2 - Oui] : ")
if str(choix)=="1":
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("Bienvenue dans l'alpha de XZ GAME !")
	time.sleep(1)
	print ("")
	print ("Cet alpha a pour but de découvrir les possibilités de build qu'offre l'arbre de talent et de découvrir la mécanique des combats")
	print ("")
	time.sleep(1)
	print ("Dans le menu prncipal, vous aurez le choix entre :")
	print ("")
	time.sleep(1)
	print ("L'expédition, qui commence directement un nouveau combat contre un poutch avec énormément de vie et réalisant la même attaque à chaque tour.")
	time.sleep(1)
	print ("Rien de très excitant mais il vous permet de tester les différents build.")
	time.sleep(1)
	print ("Vous pourrez quitter à tout moment le combat en utilisant 'quitter' pour tester d'autre chose")
	time.sleep(1)
	print ("")
	print ("Les traits qui représentent la première possibilité d'augmentation type 'arbre de talent' proposée dans le jeu")
	time.sleep(1)
	print ("Vous avez 3 choix : la Vivacité, la Puissance et la Résistance")
	time.sleep(1)
	print ("")
	print ("Enfin, les spécialisations qui sont les deuxièmes améliorations disponibles (accessible lorsque vous débloquez le dernier palier de votre trait)")
	time.sleep(1)
	print ("Vous avez également 3 choix : Insaisissable, Elementaire et Sanguinaire")
	print ("")
	time.sleep(1)
	print ("NB : Dans l'alpha, vous avez directement 18 points d'aptitudes qui permettent de compléter tous les paliers de votre trait et de votre spécialisation.")
	time.sleep(1)
	print ("Mais n'hésitez pas à tester qu'avec les premiers paliers par exemple, puisque ce sera le cas en suivant le déroulement normal du jeu !")
	time.sleep(1.5)
	print ("")
	print ("")
	input("Quand vous souhaitez continuer, appuyer sur n'importe quelle touche.")
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("Rapides explications sur les caractéristiques :")
	time.sleep(1)
	print ("	- vie : rien d'original, si vous perdez votre vie... Vous êtes mort, logique.")
	time.sleep(1)
	print ("	- force : au plus vous en avez, au plus vous tapez.")
	time.sleep(1)
	print ("	- armure : réduit les dégats subis")
	time.sleep(1)
	print ("	- vitesse : au plus vous avez de vitesse au plus vous jouez 'vite'")
	time.sleep(1.5)
	print ("")
	print ("Ce sont les 4 caractéristiques principales, jusque là rien de révolutionnaire...")
	print ("")
	time.sleep(1)
	print ("Par contre la suite :")
	time.sleep(1.5)
	print ("")
	print ("	- la technique : de 0% à 100%, représente la chance de lancer un sort en faisant une action")
	time.sleep(1)
	print ("	- la précision : de 0% à 100% représente la chance de faire un coup critique")
	time.sleep(1)
	print ("	- la brutalité : augmente les dégats critiques")
	time.sleep(1)
	print ("	- le toucher : augmente la chances de... toucher la cible !")
	time.sleep(1.5)
	print ("")
	print ("Petite explication concernant la technique, j'en profite pour passer à l'explication sur les mécanismes de combat !")
	print ("")
	input("Quand tu es prêt, appuie sur une touche")
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("En fonction de votre vitesse, soit vous commencez soit c'est l'ennemi")
	time.sleep(1)
	print ("Un bandeau informatif vous donne toutes les informations utiles lors des combats")
	time.sleep(1)
	print ("Lorsque c'est à votre tour de jouer, vous avez 3 choix possibles (puis 4 grâce aux spécialisations) :")
	time.sleep(1)
	print ("	- frappe rapide = inflige des dégats")
	time.sleep(1)
	print ("	- frappe lourde = inflige des dégats")
	time.sleep(1)
	print ("	- bouclier = augmente votre armure pour 1 tour")
	time.sleep(1.5)
	print ("")
	print ("Vous disposez de 3 points d'énergie (puis plus avec les talents et autre) pour effectuer des actions.")
	time.sleep(1)
	print ("Chacune des 3 actions ci-dessus coûtent 1 point d'énergie")
	time.sleep(1)
	print ("Chaque action a une chance (fonction de votre technique) de déclencher un sort")
	time.sleep(1)
	print ("Pour les besoins du test de cet alpha, vous n'avez pas la main sur les sorts exécutables")
	time.sleep(1)
	print ("De plus, la technique permet d'activer certains talents débloqués dans les traits et/ou les spécialisations très puissants")
	time.sleep(1.5)
	print ("Je pense que vous avez les bases")
	print ("")
	input("Pour commencer (enfin) à jouer, appuyez sur une touche")
	os.system('cls' if os.name == 'nt' else 'clear')
point_aptitude=18
vie=1000
force=325
arm=150
vit=100
preci=1
brut=50
touch=1
tech=1
liste_trait = []
with open("trait_selection.txt","r") as f_read:
	for line in f_read:
		line=line.strip()
		liste_trait.append(line)
f_read.close()
liste_specialisation = []
with open("specialisation_selection.txt","r") as f_read:
	for line in f_read:
		line=line.strip()
		liste_specialisation.append(line)
			
f_read.close()

a=1
while a==1:
	choix=menu_x_choix(1,"MENU PRINCIPAL","Expédition","Talents","Quitter")
	if str(choix)=="3":
		a=0
		pass
	elif str(choix)=="1":
		print ("en cours de dev")
	elif str(choix)=="2":
		b=1
		while b==1:
			choix=menu_x_choix(1,"TALENTS","Traits","Spécialisations","Réinitialiser","Retour")
			if str(choix)=="4":
				b=0
				pass
			elif str(choix)=="1":
				c=1
				while c==1:
					if str(liste_trait[0])=="0":
						print ("Dans un premier temps, vous allez devoir choisir votre trait.")
						input("Appuyez sur une touche lorsque vous êtes prêt...")
						d=1
						while d==1:
							choix=menu_x_choix(1,"TRAITS","Vivacité (pour ceux qui aiment jouer souvent)","Puissance (pour ceux qui aiment taper fort)","Résistance (pour ceux qui ne veulent pas mourir)","Retour")
							if str(choix)=="4":
								c=0
								d=0
								pass
							elif str(choix)=="1":
								liste_trait[0]=1
								liste_trait[1]="VIVACITE"
								d=0
							elif str(choix)=="2":
								liste_trait[0]=1
								liste_trait[1]="PUISSANCE"
								d=0
							elif str(choix)=="3":
								liste_trait[0]=1
								liste_trait[1]="RESISTANCE"
								d=0
						fw = open("trait_selection.txt","w")
						fw.write(str(liste_trait[0]))
						fw.write("\n")
						fw.write(str(liste_trait[1]))
						fw.write("\n")
						fw.write(str(liste_trait[2]))
						fw.write("\n")
						fw.write(str(liste_trait[3]))
						fw.write("\n")
						fw.write(str(liste_trait[4]))
						fw.write("\n")
						fw.write(str(liste_trait[5]))
						fw.write("\n")
						fw.write(str(liste_trait[6]))
						fw.write("\n")
						fw.write(str(liste_trait[7]))
						fw.write("\n")
						fw.write(str(liste_trait[8]))
						fw.write("\n")
						fw.write(str(liste_trait[9]))
						fw.write("\n")
						fw.write(str(liste_trait[10]))
						fw.write("\n")
						fw.write(str(liste_trait[11]))
						fw.write("\n")
						fw.write(str(liste_trait[12]))
						fw.write("\n")
						fw.write(str(liste_trait[13]))
						fw.write("\n")
						fw.write(str(liste_trait[14]))
						fw.write("\n")
						fw.write(str(liste_trait[15]))
						fw.write("\n")
						fw.write(str(liste_trait[16]))
						fw.write("\n")
						fw.write(str(liste_trait[17]))
						fw.write("\n")
						fw.write(str(liste_trait[18]))
						fw.write("\n")
						fw.write(str(liste_trait[19]))
						fw.write("\n")
						fw.write(str(liste_trait[20]))
						fw.close()
					else:
						if str(liste_trait[1])=="VIVACITE":
							talent("trait_global_vivacite.txt","trait_selection.txt",point_aptitude)
							c=0
							d=0
						elif str(liste_trait[1])=="PUISSANCE":
							talent("trait_global_puissance.txt","trait_selection.txt",point_aptitude)
							c=0
							d=0
						elif str(liste_trait[1])=="RESISTANCE":
							talent("trait_global_resistance.txt","trait_selection.txt",point_aptitude)
							c=0
							d=0
			elif str(choix)=="2":
				c=1
				while c==1:
					if str(liste_specialisation[0])=="0":
						if str(liste_trait[19])=="0":
							print ("Vous devez d'abord atteindre le dernier palier de votre trait !")
							input("Appuyez sur une touche pour continuer...")
							c=0
							pass
						else:
							print ("Dans un premier temps, vous allez devoir choisir votre spécialisation.")
							input("Appuyez sur une touche lorsque vous êtes prêt...")
							d=1
							while d==1:
								choix=menu_x_choix(1,"SPECIALISATION","Insaisissable (pour ceux qui veulent rester dans l'ombre)","Elementaire (pour ceux qui aiment la magie)","Sanguinaire (pour ceux qui... aiment le sang ?)","Retour")
								if str(choix)=="4":
									d=0
									c=0
									pass
								elif str(choix)=="1":
									liste_specialisation[0]=1
									liste_specialisation[1]="INSAISISSABLE"
									d=0
								elif str(choix)=="2":
									liste_specialisation[0]=1
									liste_specialisation[1]="ELEMENTAIRE"
									d=0
								elif str(choix)=="3":
									liste_specialisation[0]=1
									liste_specialisation[1]="SANGUINAIRE"
									d=0
							fw = open("specialisation_selection.txt","w")
							fw.write(str(liste_specialisation[0]))
							fw.write("\n")
							fw.write(str(liste_specialisation[1]))
							fw.write("\n")
							fw.write(str(liste_specialisation[2]))
							fw.write("\n")
							fw.write(str(liste_specialisation[3]))
							fw.write("\n")
							fw.write(str(liste_specialisation[4]))
							fw.write("\n")
							fw.write(str(liste_specialisation[5]))
							fw.write("\n")
							fw.write(str(liste_specialisation[6]))
							fw.write("\n")
							fw.write(str(liste_specialisation[7]))
							fw.write("\n")
							fw.write(str(liste_specialisation[8]))
							fw.write("\n")
							fw.write(str(liste_specialisation[9]))
							fw.write("\n")
							fw.write(str(liste_specialisation[10]))
							fw.write("\n")
							fw.write(str(liste_specialisation[11]))
							fw.write("\n")
							fw.write(str(liste_specialisation[12]))
							fw.write("\n")
							fw.write(str(liste_specialisation[13]))
							fw.write("\n")
							fw.write(str(liste_specialisation[14]))
							fw.write("\n")
							fw.write(str(liste_specialisation[15]))
							fw.write("\n")
							fw.write(str(liste_specialisation[16]))
							fw.write("\n")
							fw.write(str(liste_specialisation[17]))
							fw.write("\n")
							fw.write(str(liste_specialisation[18]))
							fw.write("\n")
							fw.write(str(liste_specialisation[19]))
							fw.write("\n")
							fw.write(str(liste_specialisation[20]))
							fw.close()
				else:
					if str(liste_specialisation[1])=="INSAISISSABLE":
						talent("specialisation_global_insaisissable.txt","specialisation_selection.txt",point_aptitude)
						c=0
						d=0
					elif str(liste_specialisation[1])=="ELEMENTAIRE":
						talent("specialisation_global_elementaire.txt","specialisation_selection.txt",point_aptitude)
						c=0
						d=0
					elif str(liste_specialisation[1])=="SANGUINAIRE":
						talent("specialisation_global_sanguinaire.txt","specialisation_selection.txt",point_aptitude)
						c=0
						d=0
			elif str(choix)=="3":
				os.remove("trait_selection.txt")
				os.remove("specialisation_selection.txt")
				print ("Votre trait et votre spécialisation ont été Réinitialisés.")
				print ("")
				print ("Le jeu doit être relancé...")
				print ("")
				input("Appuyez sur une touche pour fermer le jeu")
				quit()