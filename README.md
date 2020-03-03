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
	- technique (augmente les proba)
	- précision (augmente les chances de coup critique)
	- toucher (augmente tes chances de toucher)
	- brutalité (dcc)


puissance :
1) frappe lourde a une chance d'ignorer l'armure de la cible (2% + technique)
2) +3%préci / +10%brut / +2%tech
3) +3%préci / +10%brut / +2%tech
4) +3%préci / +10%brut / +2%tech
5) les cc ont une chance d'ignorer l'armure ennemi (10% + technique)
6) +3%préci / +10%brut / +2%tech
7) +3%préci / +10%brut / +2%tech
8) +3%préci / +10%brut / +2%tech
9) 1 pt d'energie en plus

vivacité :
1) frappe rapide à une chance de vous rendre 1 point d'énergie (1% + technique)
2) +2%tech / vit / +10%brut
3) +2%tech / vit / +10%brut
4) +2%tech / vit / +10%brut
5) les dégats des frappes rapides successives augmentent (seulement sur le même tour) - +10%
6) +2%tech / vit / +10%brut
7) +2%tech / vit / +10%brut
8) +2%tech / vit / +10%brut
9) 1 pt d'énergie en plus

Intouchable :
1) bouclier a une chance de bloquer l'attaque (1% + technique)
2) vie / armu / +2%tech
3) vie / armu / +2%tech
4) vie / armu / +2%tech
5) Inflige dégat d'armure lorsque vous bloquez
6) vie / armu / +2%tech
7) vie / armu / +2%tech
8) vie / armu / +2%tech
9) 1 pt d'énergie en plus

------------------------

Insaisissable :
1) +1% de chance d'esquiver (fonction technique)
2) +1%tech / +6%brut / vit
3) +1%tech / +6%brut / vit
4) +1%tech / +6%brut / vit
5) après une esquive, permet de lancer le sort 4 = contre-attaque (cc obligatoire)
6) +1%tech / +6%brut / vit
7) +1%tech / +6%brut / vit
8) +1%tech / +6%brut / vit
9) votre vitesse augmente vos chances d'esquiver

Elémentaire :
1) chance de poser un sceau en infligeant des dégats
2) +3%tech / armu / vit
3) +3%tech / armu / vit
4) +3%tech / armu / vit
5) permet d'activer 3 sceaux (sort 4 = absorption élementaire) pour lancer un sort parmi une liste aléatoire
6) +3%tech / armu / vit
7) +3%tech / armu / vit
8) +3%tech / armu / vit
9) 20% chance de conserver 1 sceau aléatoire après les avoir absorbés.

Sanguinaire :
1) infliger des dégats a 40% de chance de poser plaie sur la cible
2) +3%préci / vie / force
3) +3%préci / vie / force
4) +3%préci / vie / force
5) les cc pose plaies sur la cible
6) +3%préci / vie / force
7) +3%préci / vie / force
8) +3%préci / vie / force
9) Boucherie : consommer 10 plaies sur la cible pour infliger l'équivalent de 2 fois les dégats infligés à chaque début de tour
