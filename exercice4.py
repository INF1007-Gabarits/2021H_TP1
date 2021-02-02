def convertir_jour(j) :
    return {
        0 : "Samedi",
        1 : "Dimanche",
        2 : "Lundi",
        3 : "Mardi",
        4 : "Mercredi",
        5 : "Jeudi",
        6 : "Vendredi",
    }[j]

def trouver_jour_semaine(annee, mois, jour):
    # TODO: Calculer p
    p = 

	# TODO: Calculer q
	q = 

	# TODO: Calculer r
	r = 

	# TODO: Calculer s
	s =

	# TODO: Calculer t 
	t = 
	
	# Convertir le résultat de la formule de Zeller
	jour_semaine = convertir_jour(t)

	# TODO: Afficher le jour de la semaine

	return jour_semaine

if __name__ == '__main__':
    annee = int(input("Entrer l'annee: "))
    mois = int(input("Entrer le mois: "))
    jour = int(input("Entrer le jour: "))
    trouver_jour_semaine(annee, mois, jour)
