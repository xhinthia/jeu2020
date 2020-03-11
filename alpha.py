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
	fw.write(str("+2% de technique <OU> +6% de magie <OU> +6% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de magie <OU> +6% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de magie <OU> +6% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Les dégats successifs dans un même tour augmente (+10% à chaque itération)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de magie <OU> +6% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de magie <OU> +6% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +6% de magie <OU> +6% de force"))
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
	fw.write(str("Les coups critiques de frappe lourde ont une chance d'ignorer l'armure de la cible (20% + technique)"))
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
	fw.write(str("+2% de technique <OU> +8% de brutalité <OU> +3% de toucher"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +8% de brutalité <OU> +3% de toucher"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +8% de brutalité <OU> +3% de toucher"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Lors d'une esquive, vous débloquez le 4e sort : Contre (100% de coup critique)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +8% de brutalité <OU> +3% de toucher"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +8% de brutalité <OU> +3% de toucher"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+2% de technique <OU> +8% de brutalité <OU> +3% de toucher"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Contre attaque augmente votre esquive pour un tour (+10%)"))
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
	fw.write(str("+3% de technique <OU> +4% de toucher <OU> +9% de magie"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +4% de toucher <OU> +9% de magie"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +4% de toucher <OU> +9% de magie"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Débloque le 4e sort : Explosion élémentaire (lance un sort en fonction des éléments consommés)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +4% de toucher <OU> +9% de magie"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +4% de toucher <OU> +9% de magie"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de technique <OU> +4% de toucher <OU> +9% de magie"))
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
	fw.write(str("+3% de précision <OU> +4% de toucher <OU> +8% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +4% de toucher <OU> +8% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +4% de toucher <OU> +8% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("Vous débloquez le 4e sort : Boucherie (consomme 10 plaies pour inflger 3 fois leurs dégats périodiques)"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +4% de toucher <OU> +8% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +4% de toucher <OU> +8% de force"))
	fw.write("\n")
	fw.write(str(1))
	fw.write("\n")
	fw.write(str("+3% de précision <OU> +4% de toucher <OU> +8% de force"))
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
	print ("	- magie : augmente les dégats des sorts")
	time.sleep(1.5)
	print ("")
	print ("Ce sont les 4 caractéristiques principales, jusque là rien de révolutionnaire...")
	print ("")
	time.sleep(1)
	print ("Par contre la suite :")
	time.sleep(1.5)
	print ("")
	print ("	- la technique : représente la chance de lancer un sort en faisant une action (en pourcentage)")
	time.sleep(1)
	print ("	- la précision : représente la chance de faire un coup critique (en pourcentage)")
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
	print ("Vous commencez toujours en premier")
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

print ("Avez-vous une sauvegarde ? [oui]/[non]")
pml=input()
if pml=="oui":
	sauveg = []
	with open("sauv.txt","r") as f_read:
		for line in f_read:
			line=line.strip()
			sauveg.append(line)
	f_read.close()
	nom=sauveg[0]
	point_aptitude=sauveg[1]
elif pml=="non":
	if os.path.isfile("sauv.txt")=="true":
		os.remove("sauv.txt")
	nom=input("Quel est ton nom ? ")
	point_aptitude=18

vie_supp=0
force_supp=0
armure_supp=0
magie_supp=0
precision_supp=0
brutalite_supp=0
toucher_supp=0
technique_supp=0
energie_supp=0
vivacite_1=0
vivacite_2=0
puissance_1=0
puissance_2=0
resistance_1=0
resistance_2=0
insaisissable_1=0
insaisissable_2=0
insaisissable_3=0
elementaire_1=0
elementaire_2=0
elementaire_3=0
sanguinaire_1=0
sanguinaire_2=0
sanguinaire_3=0

a=1
while a==1:

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

	a=talent_variable(liste_trait,"1")
	b=talent_variable(liste_trait,"2")
	c=talent_variable(liste_trait,"3")
	if str(liste_trait[2])=="1":
		if str(liste_trait[1])=="VIVACITE":
			if str(liste_trait[2])=="1":
				vivacite_1=vivacite_1+1
			if str(liste_trait[10])=="1":
				vivacite_2=vivacite_2+1
			if str(liste_trait[18])=="1":
				energie_supp=energie_supp+1
			technique_supp=technique_supp+2*a
			magie_supp=magie_supp+6*b
			force_supp=force_supp+6*c
		if str(liste_trait[1])=="PUISSANCE":
			if str(liste_trait[2])=="1":
				puissance_1=puissance_1+1
			if str(liste_trait[10])=="1":
				puissance_2=puissance_2+1
			if str(liste_trait[18])=="1":
				energie_supp=energie_supp+1
			technique_supp=technique_supp+3*a
			precision_supp=precision_supp+3*b
			brutalite_supp=brutalite_supp+10*c
		if str(liste_trait[1])=="RESISTANCE":
			if str(liste_trait[2])=="1":
				resistance_1=resistance_1+1
			if str(liste_trait[10])=="1":
				resistance_2=resistance_2+1
			if str(liste_trait[18])=="1":
				energie_supp=energie_supp+1
			technique_supp=technique_supp+2*a
			vie_supp=vie_supp+7*b
			armure_supp=armure_supp+6*c

	if str(liste_specialisation[2])=="1":
		if str(liste_specialisation[1])=="INSAISISSABLE":
			if str(liste_specialisation[2])=="1":
				insaisissable_1=insaisissable_1+1
			if str(liste_specialisation[10])=="1":
				insaisissable_2=insaisissable_2+1
			if str(liste_specialisation[18])=="1":
				insaisissable_3=insaisissable_3+1
			technique_supp=technique_supp+2*a
			brutalite_supp=brutalite_supp+8*b
			toucher_supp=toucher_supp+3*c
		if str(liste_specialisation[1])=="ELEMENTAIRE":
			if str(liste_specialisation[2])=="1":
				elementaire_1=elementaire_1+1
			if str(liste_specialisation[10])=="1":
				elementaire_2=elementaire_2+1
			if str(liste_specialisation[18])=="1":
				elementaire_3=elementaire_3+1
			technique_supp=technique_supp+3*a
			toucher_supp=toucher_supp+4*b
			magie_supp=magie_supp+9*c
		if str(liste_specialisation[1])=="SANGUINAIRE":
			if str(liste_specialisation[2])=="1":
				sanguinaire_1=sanguinaire_1+1
			if str(liste_specialisation[10])=="1":
				sanguinaire_2=sanguinaire_2+1	
			if str(liste_specialisation[18])=="1":
				sanguinaire_3=sanguinaire_3+1
			precision_supp=precision_supp+3*a
			toucher_supp=toucher_supp+4*b
			force_supp=force_supp+8*c

	vie=10000+vie_supp*10000//100
	force=325+force_supp*325//100
	armure=150+armure_supp*150//100
	magie=100+magie_supp
	preci=1+precision_supp
	brut=100+brutalite_supp
	touch=1+toucher_supp
	tech=1+technique_supp
	energie=3+energie_supp

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
							choix=menu_x_choix(1,"TRAITS","Vivacité (Frapper souvent mais sûrement...)","Puissance (Désolé, je ne sens pas ma force !)","Résistance (Il faut savoir encaisser pour gagner)","Retour")
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
							point_aptitude=talent("trait_global_vivacite.txt","trait_selection.txt",point_aptitude)
							c=0
							d=0
						elif str(liste_trait[1])=="PUISSANCE":
							point_aptitude=talent("trait_global_puissance.txt","trait_selection.txt",point_aptitude)
							c=0
							d=0
						elif str(liste_trait[1])=="RESISTANCE":
							point_aptitude=talent("trait_global_resistance.txt","trait_selection.txt",point_aptitude)
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
						point_aptitude=talent("specialisation_global_insaisissable.txt","specialisation_selection.txt",point_aptitude)
						c=0
						d=0
					elif str(liste_specialisation[1])=="ELEMENTAIRE":
						point_aptitude=talent("specialisation_global_elementaire.txt","specialisation_selection.txt",point_aptitude)
						c=0
						d=0
					elif str(liste_specialisation[1])=="SANGUINAIRE":
						point_aptitude=talent("specialisation_global_sanguinaire.txt","specialisation_selection.txt",point_aptitude)
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