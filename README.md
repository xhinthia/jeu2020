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
1) les cc avec frappe lourde ignorent 10% armure
2) précision / brutalité / technique
3) soit préci + bruta soit préci + tech soit bruta + tech
4) précision / brutalité / technique
5) +10% arpen / +1% chance de stun
6) précision / brutalité / technique
7) +15% arpen / +100% arpen sur les cibles stun
8) soit préci + bruta soit préci + tech soit bruta + tech
9) 1 pt d'energie en plus

vivacité :
1) frappe rapide à une chance de vous rendre 1 point d'énergie
2) technique / vitesse / brutalité
3) tech + vit / tech + brut / vit + brut
4) tech / vit / brut
5) Effectuer 5 frappe rapides, augmente votre vitesse pour le reste du cbt / les frappes rapides successives infligent plus de dégats
6) tech / vit / brut
7) +30% de chance vous rendre 2 points d'énergie au lieu de 1 / la 5e frappes successives est un coup critique
8) tech + brut / tech + brut / vit + brut
9) 1 pt d'énergie en plus

Intouchable :
1) bouclier a une chance de bloquer l'attaque (-25% dégat)
2) vie / armure / technique
3) vie + technique / vie + armure / technique + armure
4) vie / armure / technique
5) Inflige dégat d'armure lorsque vous bloquez / blocage puissant (-50% dégat)
6) vie / armure / technique
7) blocage vous rend de la vie / blocage parfait (-80% dégat)
8) vie + armure / vie + technique / technique + armure
9) 1 pt d'énergie en plus

------------------------

Insaisissable :
1) ta vitesse augmente tes chances d'esquiver
2) agi / brut / vitesse
3) agi + brut / agi + vitesse / vit + burt
4) agi / brut / vit
5) après une esquive, permet de lancer le sort 4 = contre-attaque (cc obligatoire)
6) agi / brut / vitesse
7) agi + brut / agi + vit / brut + vit
8) agi / brut / vit
9) augmente vos chances d'esquiver lorsque tu perds de la vie

Elémentaire :
1) chance de poser un sceau en infligeant des dégats
2) technique / vie / vitesse
3) tech + vie / vie + vit / tech + vit
4) technique / armure / vitesse
5) permet d'activer 3 sceaux (sort 4 = absorption élementaire) pour lancer un sort parmi une liste aléatoire
6) technique / vie / vitesse
7) tech + armure / tech + vit / vit + armure
8) tech / armure / vitesse
9) faible chance de conserver 1 sceau aléatoire après les avoir absorbés.

Sanguinaire :
1) les coups critiques infligent plaie sur la cible
2) préci / vie / force
3) préci + for / vie + for / préci + vie
4) préci / vie / force
5) Utilise le reste de tes points d'énergie pour infliger autant de plaie sur la cible, permet 1 pt d'énergie pour le reste du combat
6) préci / vie / force
7) préci + vie / préci + for / vie + for
8) préci / vie / force
9) 30% de chance de ne pas perdre de pt d'énergie
