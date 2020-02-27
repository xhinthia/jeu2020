import os
import sys
from modules.combat import *
from modules.utilitaires import *








resultat=pick_number(50,100)
print (resultat)
input()


print ("1 - Combat")
a=0
while a==0: 
    choix=input("Que veux-tu faire ? ")
    if str(choix)=='1':
        combat(100,10,10,100,10,10)
        a=1
    else:
        pass
    
