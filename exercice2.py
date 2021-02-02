import math


def resoudre_equation(a, b, c):
    # TODO: Calculer le discriminant et assigner la valeur dans la variable "delta"
    

    # TODO: Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
    naPasDeSolution = 

    if naPasDeSolution:
        # ces ligne de code seront executé si il y'a aucune racine
        # TODO: afficher sur l'écran "Aucune racine"
        
        # ne pas modifier
        return None

    # TODO: Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    aUneSeuleSolution = delta == 0

    if aUneSeuleSolution:
        # ces ligne de code seront executé si il y'a une seule racine
        
        # TODO: afficher sur l'écran "Une seule racine"
        
        # TODO: assigner a la variable x1 la valeur de la racine
        
        # ne pas modifier
        return x1

    # TODO: Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    aDeuxSolutions = 

    if aDeuxSolutions:
        # TODO: afficher sur l'écran "Deux racines"
        

        # TODO: calculer la prmiere racine, assigner la a "x1"
        

        # TODO: calculer la deuxieme racine, assigner la a "x2"
        

        # ne pas modifier cette ligne
        return x1, x2


if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

    print(resoudre_equation(a, b, c))
