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

def affichage_global(clean,titre,*arg):
	if clean==1:
		os.system('cls' if os.name == 'nt' else 'clear')
	print ("**********************************")
	print ("")
	print ("	"+str(titre))
	print ("")
	print ("**********************************")
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")
	print ("")
	j=1
	for i in (arg):
		print ("Palier "+str(j)+" : "+str(i))
		j+=1
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")
	input()

def selection_trait(point_aptitude,trait0,trait1,trait2,trait3,trait4,trait5,trait6,trait7,trait8,trait9):
	a=1
	while a==1:
		if clean==1:
			os.system('cls' if os.name == 'nt' else 'clear')
		print ("**********************************")
		print ("")
		print ("	"+str(trait0))
		print ("")
		print ("**********************************")
		print ("")
		print ("<><><><><><><><><><><><><><><><><>")
		print ("")
		j=0
		for i in (1,9):
			j+=1
			if str(trait+i)=="0":
				pass
			else:
				print ("Palier "+str(j)+" : "+str(trait+i))
			print ("")
			print ("<><><><><><><><><><><><><><><><><>")
		if str(trait0)=="Vivacité":
			if j==1:
				b=1
				while b==1:
					choix=menu_x_choix(0,"PALIER "+j,"Frappe rapide a une chance de vous rendre 1 point d'énergie (1% + technique)","Retour")
					if str(choix)=="2":
						b=0
						pass
					elif str(choix)=="1":
						trait1="Frappe rapide a une chance de vous rendre 1 point d'énergie (1% + technique)"
						b=0
						pass
					elif str(choix)=="2":
						a=0
						b=0
						pass
			elif (j>1 and j<5):
				b=1
				while b==1:
					choix=menu_x_choix(0,"PALIER "+j,"+2% technique","+X% vitesse","+10% brutalité","Retour")
					if str(choix)=="4":
						b=0
						pass
					elif str(choix)=="1":
						(trait+j)=
		elif str(trait0)=="Puissance":

		elif str(trait0)=="Résistance":

def selection_trait_perso(clean,trait,*arg):
	if clean==1:
		os.system('cls' if os.name == 'nt' else 'clear')
	liste = []
	with open("trait.txt","r") as f_read:
		for line in f_read:
			line=line.strip()
			liste.append(line)
	f_read.close()
	p0 = liste[0]
	p1 = liste[1]
	p2 = liste[2]
	p3 = liste[3]
	p4 = liste[4]
	p5 = liste[5]
	p6 = liste[6]
	p7 = liste[7]
	p8 = liste[8]
	p9 = liste[9]
	if str(p0)=="1":
		p0="Vivacité"
		p1="frappe rapide à 5% de chance de vous rendre 1 point d'énergie"
		if str(p2)=="1":
			p2="+3% de technique"
		elif str(p2)=="2":
			p2="+3% de vitesse"
		elif str(p2)=="3":
			p2=""
	elif str(p0)=="2":
		p0="Puissance"
	elif str(p0)=="3":
		p0="Résistance"
	print ("**********************************")
	print ("")
	print ("	"+str(p0))
	print ("")
	print ("**********************************")
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")
	print ("")
	j=1
	for i in (arg):
		print ("Palier "+str(j)+" : "+str(i))
		j+=1
	print ("")
	print ("<><><><><><><><><><><><><><><><><>")
	input()


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

a=1
i=0
while a==1:
	i+=1
	if str(p+i)=="0":
		a=0
		pass
