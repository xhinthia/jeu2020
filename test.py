import os
import sys
import os.path
import random

a1=1
a2="blabla"
a3=1
a4="XXXXX"
a5=1
a6="gniagnia"
a7=1
a8="test"
a9=1
a10="test2"
a11=0
a12="test encore"
a13=0
a14="et toujours"
a15=0
a16="j'en ai marre"
a17=0
a18="pourvu que ca marche"
liste = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18]
"""j=1
for i in liste:
	if i==0:
		pass
	else:
		print ("Palier "+str(j)+" : "+str(i))
	j+=1
input()"""

x=0
for x in range (0,18,2):
	if liste[x]!=0:
		print (liste[x+1])
	else:
		break
input()