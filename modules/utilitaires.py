import os
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

def menu_3_choix(titre,choix_1,choix_2,choix_3,choix_0):
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("**********************************")
	print ("")
	print ("	"+str(titre))
	print ("")
	print ("**********************************")
	print (" ")
	print ("<><><><><><><><><><><><><><><><><>")
	print ("")
	print ("1 > "+str(choix_1))
	print ("")
	print ("2 > "+str(choix_2))
	print ("")
	print ("3 > "+str(choix_3))
	print ("")
	print ("0 > "+str(choix_0))
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")
	choix=input()
	return choix
