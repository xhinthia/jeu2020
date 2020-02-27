import os
import sys

def combat(viem,forcem,armurem,vie,force,armure):
    os.system('cls' if os.name == 'nt' else 'clear')
    while int(vie)>0 and int(viem)>0:
        armure=10
        print ("1 - Frappe rapide")
        print ("2 - Frappe précise")
        print ("3 - Bouclier")
        choix=input("Que veux-tu faire ? ")
        if str(choix)=='1':
           print ("Vous infligez 10 points de dégat à la cible !")
           viem -= 10-armurem
        elif str(choix)=='2':
            print ("Vous infligez 10 poiints de dégat à la cible !")
            viem -= 10-armurem
        elif str(choix)=='3':
            print ("Votre armure augmente pour le prochain coup !")
            armure += 10
        else:
            print ("tes choix sont malheureusement limités...")
            pass
        if viem < 0:
            print ("la cible est morte...")
            pass
        else:
            print ("La cible utilise morsure !")
            vie -= 30-armure
    if viem < 0:
        print ("Bravo vous avez gagné !")
    elif vie < 0:
        print ("Vous êtes mort...")
    else:
        pass
