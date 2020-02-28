# jeu2020

frappe rapide : inflige des dégats + 1% chance rejouer
frappe lourde : inflige des dégats + 1% cc
bouclier : augmente l'armure + % chance de bloquer % dégats

Traits = 1e palier
	- Vivacité :
		1) Quand frappe rapide, % de chance de rejouer (certains mobs enrage à chaque fois que vous jouez : stack qui monte à chaque action)
		2) Quand vous gagnez un tour avec frappe rapide, augmente vos dégats pour ce tour

	- Puissance :
		1) frappe lourde à % chance de stun la cible (certains mob sont insensible au stun)
		2) frappe lourde à +% chance d'ignorer sur les cibles stun

	- Résistance :
		1) Quand vous bloquez inflige un coup de bouclier (fonction de votre armure)
		2) % chance quand vous bloquez de récupérer des pv

Spécialisations = 2e palier
	- Insaisissable :
		1) % chance d'esquiver les dégats (passe avant le blocage)
		2) Quand vous esquivez, vous pouvez utiliser le 4e sort qui consomme 2 energie (cc obligatoire)

	- Elémentaire :
		1) % chance de placer un sceau (feu, foudre, glace)
		2) consomme 3 sceaux avec le 4e sort

	- Sanguinaire :
		1) % chance d'infliger plaie à la cible (inflige des dégats à chaque début de tour et peut se cumuler)
		2) Utilise 3 points d'énergie pour double les stacks de plaie

Maîtrise = 3e palier
	- Surpuissance : augmente les % de puissance et de sanguinaire
	- Transcendance : augmente les % de vivacité et de élem
	- Perseverance : augmente les % de résistance et de insaisissable
	- Fulgurance : augmente les % de vivacité et de insaisissable
	- Predominance : vivacité + sanguinaire
	- Arrogance : puissance + insaisissable
	- Flamboyance : puissance + elementaire
	- Clairvoyance : résistance + elem
	- Souffrance : résistance + sanguinaire


caractéristique:
	- Vie
	- Force
	- Armure
	- vitesse
	- technique (augmente les chances de réaliser un sort)
	- précision (augmente les chances de toucher)
	- ténacité (chance de résister à un effet de statut)
	- brutalité (dcc ou %arpen si 7)


puissance :
1) +10% cc frappe lourde
2) Force / vie
3) +10% cc
4) brutalité / technique
5) +10% cc / si cc -> 30%arpen
6) force / vie / force et vie
7) -force +20%cc + 25%dcc /  60%arpen lors d'un cc
8) brutalité / technique / les 2
9) 1 pt d'energie en plus


vivacité :
1) 5% rejouer
2) force / vitesse
3) +5% rejouer
4) précision / technique
5) Si rejouer augmente vitesse / si rejouer augmente force
6) force / vitesse / force et vitesse
7) +10% rejouer mais n'augmente plus force ou vitesse / -5% rejouer mais augmente la force et la vitesse
8) précision / technique / les 2
9) 1 pt d'énergie en plus

résistance :
1) 10% chance de bloquer
2) vie / armure
3) 10% chance de bloquer
4) ténacité / technique
5) 20% blocage / lorsque bloque inflige des dégat en fonction de l'armure
6) vie / armure / les 2
7) augmente les chances de blocage mais réduit la réduction de dégat / réduit les chances de blocage mais augmente la réduction de dgt
8) ténacité / technique / les 2
9) 1 pt nrj

------------------------

Insaisissable :
1) 
2)
3)
4)
5) % chance de esquive
6)
7)
8)
9) après une esquive vous pouvez contre-attaquer (cc obligatoire)

Elémentaire :
1) technique / 
2)
3)
4)
5) % place un sceau sur la cible (parmi feu, glace, foudre) max 3 (dépend de la technique)
6)
7)
8)
9) permet d'activer 3 sceaux et lancer un sort en fonction

Sanguinaire :
1) 
2)
3)
4)
5) les coup ont une chance d'infliger plaie sur la cible (les cc ont 2 fois plus de chance)
6)
7)
8)
9) Torture : intensifie les plaies mais réduit votre force
