import os
import os.path
import sys
import random

def pick_number(chance,total):
    difference=total-chance
    liste = []
    for i in range (0,chance):
        liste.append(1)
    for i in range (0,difference):
        liste.append(0)
    a=random.choice(liste)
    return a

def menu_x_choix(clean,titre,*arg):
	if clean==1:
		os.system('cls' if os.name == 'nt' else 'clear')
	print ("**********************************")
	print ("")
	print ("	"+str(titre))
	print ("")
	print ("**********************************")
	print (" ")
	print ("<><><><><><><><><><><><><><><><><>")
	print ("")
	j=1
	for i in (arg):
		print (str(j)+" > "+str(i))
		j+=1
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")
	choix=input()
	return choix

def bandeau(clean,etape):
	if clean==1:
		os.system('cls' if os.name == 'nt' else 'clear')
	print ("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
	print ("")
	print ("										ETAPE "+str(etape))
	print ("")
	print ("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
	print ("")
	print ("___________________________________________________________________________________________________________________________________")
	print (" ")
	print ("carac perso")
	print ("___________________________________________________________________________________________________________________________________")

def bandeau_combat(clean,):
	if clean==1:
		os.system('cls' if os.name == 'nt' else 'clear')
	print ("___________________________________________________________________________________________________________________________________")
	print ("")
	print ("carac perso")
	print ("___________________________________________________________________________________________________________________________________")
	print (" ")
	print ("carac ennemi")
	print ("___________________________________________________________________________________________________________________________________")
