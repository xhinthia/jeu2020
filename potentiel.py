import sys
import os
import os.path
import random
from utilitaires import *


#si tu choisis vivacité, tu lis le fichier vivacité.txt pour remplir la liste proposition. Ensuite tu boucles, tant que tu as des points d'aptitude, tu passes au suivant

def lecture_trait():
	liste = []
	with open("trait.txt","r") as f_read:
		for line in f_read:
			line=line.strip()
			liste.append(line)
	f_read.close()
	trait=liste[0]
	p1=liste[1]
	p2=liste[2]
	p3=liste[3]
	p4=liste[4]
	p5=liste[5]
	p6=liste[6]
	p7=liste[7]
	p8=liste[8]
	p9=liste[9]

def affichage_trait():
	