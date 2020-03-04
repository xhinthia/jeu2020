import os
import sys
import os.path

"""
affichager en grand le trait donc soir VIVACITE soit PUISSANCE soit RESISTANCE dans un cadre en haut de page (après un clear donc)
---------------
TRAITS
---------------

Puis un titre Possibilités
****************
Possibilités
****************

le listing des palier :
Palier 1 : XXXXXXXX
Palier 2 : XXXXXX ou XXXXX ou XXXXX

pour afficher au dessus on peut lire dans un fichier trait_global.txt
FONCTION DU DESSUS

**************
SELECTIONS
**************

Palier 1 : XXXX
Palier 2 : XXX

fichier trait_selection.txt palier 1 : o ou 1, palier 2 : 0, 1 , 2 ou 3 etc


si tu n'as plus de point (appuie pour sortir) :> permet de consulter + voir vos talents
if str(point_aptitude)=="0":
    tu n'as plus de point d'aptitude
    input("Appuyez sur une touche pour sortir")
else:
    Il te reste X points d'aptitude
    Voulez-vous les utiliser ?
    if oui :
        menu_x_choix(palier suivant) -> on peut utiliser un fichier trait_choix.txt avec par ex la ligne 3 pour palier 3 : "+X% technique","+X% brutalité"
        et intégrer directement la ligne dans le menu_x_choix
    else:
        input("appuyez sur une touche pour sortir")

"""

def affichage_talent(clean,fichier):
    liste = []
    with open(fichier,"r") as f_read:
        for line in f_read:
            line=line.strip()
            liste.append(line)
    f_read.close()
    if clean==1:
		os.system('cls' if os.name == 'nt' else 'clear')
	print ("**********************************")
	print ("")
	print ("	"+str(liste[0]))
	print ("")
	print ("**********************************")
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")
	print ("")
	j=1
	for i in liste:
            if i==0:
                pass
            else:
                print ("Palier "+str(j)+" : "+str(i))
            j+=1
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")

