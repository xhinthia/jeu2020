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

def talent(fichier1,fichier2,point_aptitude):
    a=1
    while a==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        liste1 = []
        with open(fichier1,"r") as f_read:
            for line in f_read:
                line=line.strip()
                liste1.append(line)
        f_read.close()
        print ("**********************************")
        print ("")
        print ("	"+str(liste1[1]))
        print ("")
        print ("**********************************")
        print ("")
        print ("<><><><><><><><><><><><><><><><><>")
        print ("")
        x=0
        y=1
        for x in range (2,18,2):
            if liste1[x]!=0:
                print ("Palier "+str(y)+" : "+str(liste1[x+1]))
                y+=1
            else:
                pass
        print ("")
        print ("<><><><><><><><><><><><><><><><><>")

        print ("")
        print ("")

        liste2 = []
        with open(fichier2,"r") as f_read:
            for line in f_read:
                line=line.strip()
                liste2.append(line)
        f_read.close()
        print ("**********************************")
        print ("")
        print ("    "+str(liste2[1]))
        print ("")
        print ("**********************************")
        print ("")
        print ("<><><><><><><><><><><><><><><><><>")
        print ("")
        i=0
        j=1
        for i in range (2,18,2):
            if liste2[i]!=0:
                print ("Palier "+str(j)+" : "+str(liste2[i+1]))
                j+=1
            else:
                pass
        print ("")
        print ("<><><><><><><><><><><><><><><><><>")

        print (" ")
        print (" ")

        if j==10:
            print ("Vos choix ont tous été faits ici !")
            input("Appuyez sur une touche pour sortir")
            a=0
            pass
        print (str(point_aptitude)+" points à dépenser")
        if point_aptitude==0:
            input("Appuyez sur une touche pour sortir")
            a=0
            pass
        else:
            choix=input("Voulez-vous utilisez vos points ? (1 - Oui, 2 - Non) : ")
            print ("")
            b=1
            while b==1:
                if str(choix)=="2":
                    input("Appuyez sur une touche pour sortir")
                    a=0
                    b=0
                    pass
                elif str(choix)=="1":
                    if liste2[1]=="VIVACITE":

                    elif liste2[1]=="PUISSANCE":

                    elif liste2[1]=="RESISTANCE":

                    elif liste2[1]=="INSAISISSABLE":

                    elif liste2[1]=="ELEMENTAIRE":

                    elif liste2[1]=="SANGUINAIRE":



        p=x//2
    prop=x+1
    with open("trait_selection.txt","r") as f_read:
        for line in range (1):
            trait = f_read.readline()
    f_read.close()
    print ("")
    print ("")
    if point_aptitude==0:
        print ("Vous n'avez plus de points à dépenser")
        input("Appuyez sur une touche pour sortir")
        a=0
        pass
    else:
        print ("Tu as "+str(point_aptitude)+" à dépenser")
        b=1
        while b==1:
            choix=input("Voulez-vous les utiliser ? (1 - Oui, 2- Non) : ")
            print ("")
            if str(choix)=="1":
                if str(trait)=="VIVACITE"
                c=1
                while c==1:
                    

            elif str(choix)=="2":
                input("Appuyez sur une touche pour sortir")
                a=0
                b=0
                pass

