import os
import sys
import os.path
from utilitaires import *

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
            if str(liste2[i])=="0":
                pass
            else:
                print ("Palier "+str(j)+" : "+str(liste2[i+1]))
                j+=1
        print ("")
        print ("<><><><><><><><><><><><><><><><><>")

        print (" ")
        print (" ")

        if j==10:
            print ("Vos choix ont tous été faits ici !")
            input("Appuyez sur une touche pour sortir")
            a=0
            pass
        print ("    > "+str(point_aptitude)+" points à dépenser <")
        print ("")
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
                        if j==1:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Frappe rapide a une chance de vous rendre 1 point d'énergie (1% + technique)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Frappe rapide a une chance de vous rendre 1 point d'énergie (1% + technique)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==5:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Les dégats successifs dans un même tour augmente (+10% à chaque itération)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Les dégats successifs dans un même tour augmente (+10% à chaque itération)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==9:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"+1 point d'énergie","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="+1 point d'énergie"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        else:
                            c=1
                            while c==1:
                                index=j*2
                                valeur=j*2+1
                                choix=menu_x_choix(0,"PALIER "+str(j),"+2% de technique","+6% de vitesse","+10% de brutalité","Retour")
                                if str(choix)=="4":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    liste2[index]=1
                                    liste2[valeur]="+2% de technique"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="2":
                                    liste2[index]=2
                                    liste2[valeur]="+6% de vitesse"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="3":
                                    liste2[index]=3
                                    liste2[valeur]="+10% de brutalité"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                    elif liste2[1]=="PUISSANCE":
                        if j==1:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Frappe lourde a une chance d'ignorer l'armure de la cible (2% + technique)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Frappe lourde a une chance d'ignorer l'armure de la cible (2% + technique)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==5:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Les coups critiques de frappe lourde ont une chance d'ignorer l'armure de la cible (15% + technique)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Les coups critiques de frappe lourde ont une chance d'ignorer l'armure de la cible (15% + technique)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==9:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"+1 point d'énergie","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="+1 point d'énergie"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        else:
                            c=1
                            while c==1:
                                index=j*2
                                valeur=j*2+1
                                choix=menu_x_choix(0,"PALIER "+str(j),"+3% de technique","+3% de précision","+10% de brutalité","Retour")
                                if str(choix)=="4":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    liste2[index]=1
                                    liste2[valeur]="+3% de technique"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="2":
                                    liste2[index]=2
                                    liste2[valeur]="+3% de précision"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="3":
                                    liste2[index]=3
                                    liste2[valeur]="+10% de brutalité"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                    elif liste2[1]=="RESISTANCE":
                        if j==1:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Bouclier a une chance de bloquer l'attaque (1% + technique)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Bouclier a une chance de bloquer l'attaque (1% + technique)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==5:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Blocage inflige des dégats (50% de votre armure)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Blocage inflige des dégats (50% de votre armure)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==9:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"+1 point d'énergie","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="+1 point d'énergie"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        else:
                            c=1
                            while c==1:
                                index=j*2
                                valeur=j*2+1
                                choix=menu_x_choix(0,"PALIER "+str(j),"+2% de technique","+7% de vie","+6% d'armure","Retour")
                                if str(choix)=="4":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    liste2[index]=1
                                    liste2[valeur]="+2% de technique"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="2":
                                    liste2[index]=2
                                    liste2[valeur]="+7% de vie"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="3":
                                    liste2[index]=3
                                    liste2[valeur]="+6% d'armure"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                    elif liste2[1]=="INSAISISSABLE":
                        if j==1:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Vous avez une chance d'esquiver une attaque (1% + technique)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Vous avez une chance d'esquiver une attaque (1% + technique)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==5:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Lors d'une esquive, vous débloquez le 4e sort : Contre (100% de coup critique)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Lors d'une esquive, vous débloquez le 4e sort : Contre (100% de coup critique)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==9:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Votre vitesse augmente vos chances d'esquive (10% de votre vitesse)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Votre vitesse augmente vos chances d'esquive (10% de votre vitesse)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        else:
                            c=1
                            while c==1:
                                index=j*2
                                valeur=j*2+1
                                choix=menu_x_choix(0,"PALIER "+str(j),"+2% de technique","+6% de vitesse","+6% de brutalité","Retour")
                                if str(choix)=="4":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    liste2[index]=1
                                    liste2[valeur]="+2% de technique"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="2":
                                    liste2[index]=2
                                    liste2[valeur]="+6% de vitesse"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="3":
                                    liste2[index]=3
                                    liste2[valeur]="+6% de brutalité"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                    elif liste2[1]=="ELEMENTAIRE":
                        if j==1:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Vous avez une chance de marquer la cible en infligeant des dégats (3 marques max): feu, foudre ou glace (1% + technique)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Vous avez une chance de marquer la cible en infligeant des dégats (3 marques max): feu, foudre ou glace (1% + technique)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==5:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Débloque le 4e sort : Explosion élémentaire (lance un sort en fonction des éléments consommés)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Débloque le 4e sort : Explosion élémentaire (lance un sort en fonction des éléments consommés)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==9:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Vous avez une chance de conserver une marque élémentaire sur votre cible après les avoir consommées (30% de chance)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Vous avez une chance de conserver une marque élémentaire sur votre cible après les avoir consommées (30% de chance)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        else:
                            c=1
                            while c==1:
                                index=j*2
                                valeur=j*2+1
                                choix=menu_x_choix(0,"PALIER "+str(j),"+3% de technique","+5% d'armure","+4% de vitesse","Retour")
                                if str(choix)=="4":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    liste2[index]=1
                                    liste2[valeur]="+3% de technique"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="2":
                                    liste2[index]=2
                                    liste2[valeur]="+5% d'armure"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="3":
                                    liste2[index]=3
                                    liste2[valeur]="+4% de vitesse"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                    elif liste2[1]=="SANGUINAIRE":
                        if j==1:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Vous avez une chance de poser plaie sur la cible en infligeant des dégats (40% de chance)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Vous avez une chance de poser plaie sur la cible en infligeant des dégats (40% de chance)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==5:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Vous débloquez le 4e sort : Boucherie (consomme 10 plaies pour inflger 3 fois leurs dégats périodiques)","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=j*2+1
                                    liste2[index]=1
                                    liste2[valeur]="Vous débloquez le 4e sort : Boucherie (consomme 10 plaies pour inflger 3 fois leurs dégats périodiques)"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        elif j==9:
                            c=1
                            while c==1:
                                choix=menu_x_choix(0,"PALIER "+str(j),"Les coups critiques posent 2 plaies sur la cible","Retour")
                                if str(choix)=="2":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    index=j*2
                                    valeur=(j*2+1)
                                    liste2[index]=1
                                    liste2[valeur]="Les coups critiques posent 2 plaies sur la cible"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                        else:
                            c=1
                            while c==1:
                                index=j*2
                                valeur=j*2+1
                                choix=menu_x_choix(0,"PALIER "+str(j),"+3% de précision","+6% de vie","+7% de force","Retour")
                                if str(choix)=="4":
                                    input("Appuyez sur une touche pour sortir")
                                    b=0
                                    c=0
                                    pass
                                elif str(choix)=="1":
                                    liste2[index]=1
                                    liste2[valeur]="+3% de précision"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="2":
                                    liste2[index]=2
                                    liste2[valeur]="+6% de vie"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                                elif str(choix)=="3":
                                    liste2[index]=3
                                    liste2[valeur]="+7% de force"
                                    b=0
                                    c=0
                                    point_aptitude-=1
                    fw = open(fichier2,"w")
                    fw.write(str(liste2[0]))
                    fw.write("\n")
                    fw.write(str(liste2[1]))
                    fw.write("\n")
                    fw.write(str(liste2[2]))
                    fw.write("\n")
                    fw.write(str(liste2[3]))
                    fw.write("\n")
                    fw.write(str(liste2[4]))
                    fw.write("\n")
                    fw.write(str(liste2[5]))
                    fw.write("\n")
                    fw.write(str(liste2[6]))
                    fw.write("\n")
                    fw.write(str(liste2[7]))
                    fw.write("\n")
                    fw.write(str(liste2[8]))
                    fw.write("\n")
                    fw.write(str(liste2[9]))
                    fw.write("\n")
                    fw.write(str(liste2[10]))
                    fw.write("\n")
                    fw.write(str(liste2[11]))
                    fw.write("\n")
                    fw.write(str(liste2[12]))
                    fw.write("\n")
                    fw.write(str(liste2[13]))
                    fw.write("\n")
                    fw.write(str(liste2[14]))
                    fw.write("\n")
                    fw.write(str(liste2[15]))
                    fw.write("\n")
                    fw.write(str(liste2[16]))
                    fw.write("\n")
                    fw.write(str(liste2[17]))
                    fw.write("\n")
                    fw.write(str(liste2[18]))
                    fw.close()
                    return point_aptitude