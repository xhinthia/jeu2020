import os
import os.path
import sys
import random
from modules.utilitaires import *
import time

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
			combat
		elif str(choix)=="2":
			b=1
			while b==1:
				choix=menu_x_choix(1,"TRAITS","Choisir","Consulter","Réinitialiser","Retour")
				if str(choix)=="4":
					b=0
					pass
				elif str(choix)=="1":
					

else:
	print ("Tu n'es pas foutu de taper 1 ou 2...? Ca promet pour jouer !")
	input()
	quit()
