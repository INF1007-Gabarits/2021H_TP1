# TP1

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 27 septembre 2020 à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200927T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif

Ce TP a pour objectif de vous introduire à l'algorithmie avec le langage de programmation Python.
Celui-ci est composé de 5 exercices, pour lesquels vous devez compléter le code avec l'indicateur `TODO`.

## Grilles de correction
Le TP est sur 20. Chaque question compte pour 4 points.

Un bon résultat donnera la note de 4/4. Une erreur minime (une erreur de tape par exemple) mènera à une pénalité de 0.5 point. Une erreur majeure (erreur dans un symbole arithmétique, question non répondue, ...) ménera à une pénalité de 1 à 4 points.

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir lu le fichier [instructions.md](instructions.md) et d'avoir téléchargé les fichiers exercices1-5.py que vous devrez compléter.
Pour ce TP, certaines contraintes sont à respecter:
- Vous ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers.
- Il est interdit de manipuler des chaînes de caractère.
- Il est interdit d'utiliser les structures de répétitions (for, while).

## Exercice 1:
Dans cet exercice, vous devez calculer la portée d'un canon. Le programme commence en demandant à l'utilisateur de saisir l'agle en degré du canon et la vitesse (en km/h) du projectile, il suffit de compléter la fonction `calculer_portee()`.
```python
    def calculer_portee(angle, vitesse):
        # TODO convertir la vitesse en metre par seconde, assigner la valeur à la variable "vitesse"
        vitesse= 
        
        # TODO calculer la portee, assigner la valeur à la variable "portee"
        portee= 
        
        return portee
```

Les points seront donnés dans la conversion de la vitesse et dans le calcul de la portée.

## Exercice 2:
Dans cet exercice, vous devez résoudre une équation quadratique de la forme <img src="https://render.githubusercontent.com/render/math?math=ax^2"> + <img src="https://render.githubusercontent.com/render/math?math=bx"> + <img src="https://render.githubusercontent.com/render/math?math=c">. Le programme commence en demandant à l'utilisateur de saisir la valeur des variables `a`, `b` et `c`. Il suffit de compléter la fonction `resoudreEquation()`.
```python
    def resoudreEquation(a, b, c):
    # TODO: Calculer le discriminant et assigner la valeur dans la variable "delta"
    delta =

    # TODO: Déterminer la condition (bool) qui correspond à la situation où l'équation n'a aucune solution et m assigner le résultat dans la variable "naPasDeSolution"
    naPasDeSolution =

    if naPasDeSolution:
        # ces lignes de code seront executé si il y'a aucune racine
        # TODO: afficher sur l'écran "Aucune racine"

        # ne pas modifier
        return None

    # TODO: Déterminer la condition (bool) qui correspond à la situation où il existe une seule solution à l'équation et mettre la valeur dans "aUneSeuleSolution"
    aUneSeuleSolution =

    if aUneSeuleSolution:
        # ces ligne de code seront executées s'il y'a une seule racine
        # TODO: affichez sur l'écran "Une seule racine"

        # TODO: assignez a la variable x1 la valeur de la racine
        x1 =
        # ne pas modifier
        return x1

    # TODO: Déterminer la condition (bool) qui correspond à la situation où il existe deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    aDeuxSolutions =

    if aDeuxSolutions:
        # TODO: affichez sur l'écran "Deux racines"

        # TODO: calculez la première racine, assignez la a "x1"
        x1 =

        # TODO: calculez la deuxième racine, assignez la a "x2"
        x2 =

        # ne pas modifier cette ligne
        return x1, x2
```
## Exercice 3:
Dans cet exercice, vous devez calculer le nombre d'unités, de dizaines et de centaines d'un nombre indiqué par l'utilisateur. Cepandant, vous ne pouvez utiliser que les fonctions de la libraire Math. Je rappelle qu'il est interdit d'utiliser les chaines de caractères!
```python
    def calculer_unites_dizaines_centaine(nombre):

        # TODO: Déterminer le nombre d'unités et mettre la valeur dans "unites"
        unites = 

        # TODO: Déterminer le nombre de dizaines et mettre la valeur dans "dizaines"
        dizaines = 

        # TODO: Déterminer le nombre de centaines et mettre la valeur dans "centaines"
        centaines = 

        # TODO: Afficher les valeurs de "unites", "dizaines" et "centaines"

        return (unites, dizaines, centaines)
```
## Exercice 4:
Dans cet exercice vous devez convertir une date (jour, mois, année) entré par l'utilisateur en jour de la semaine. Par exemple, si l'utilisateur entre 4 pour le jour, 2 pour le mois et 2021 pour l'année,la fonction va retourner jeudi. Pour cela, nous allons utiliser la formule de la congruence de Zeller.

![Zeller's congruence](https://wikimedia.org/api/rest_v1/media/math/render/svg/0f95195dcc0d98b351294277071736e97053324e)

Afin de vous faciliter la tâche, la formule a été simplifié en plusieurs étapes.

![p](https://latex.codecogs.com/svg.latex?p=\left\lfloor\dfrac{14-mois}{12}\right\rfloor)

![q](https://latex.codecogs.com/svg.latex?q=annee-p)

![r](https://latex.codecogs.com/svg.latex?r=q+\left\lfloor\dfrac{q}{4}\right\rfloor-\left\lfloor\dfrac{q}{100}\right\rfloor+\left\lfloor\dfrac{q}{400}\right\rfloor)

![s](https://latex.codecogs.com/svg.latex?s=mois+12*p-2)

![t](https://latex.codecogs.com/svg.latex?t=(\left\lfloor\dfrac{jour+r+31*s}{12}\right\rfloor)\mod7)

Une fois ces étapes finies, le résultat t est convertir en jour. Finalement, il faut l'afficher.

```python
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
```
## Exercice 5:
Un permis de chasse à point remplace désormais le permis de chasse traditionnel. Chaque chasseur possède au départ un capital de 100 points. Si le chasseur tue un Dindon, il perd 1 point, 3 points pour un Lièvre, 5 points pour un cerf et 10 points pour un ours noir. Le permis coûte 300$.

Dans cet exercice, vous devez compléter la fonction pointsperdu qui reçoit le nombre de proies du chasseur de chaque espèce et qui renvoie le nombre de points disponible.

```python
def points_perdu(dindon, lievre, cerf, ours_noir):

    # TODO: Calculer le nombre de points disponible 
    nombre_points = 100 - dindon + 3*lievre + 5*cerf + 10*ours_noir
	
    # TODO: Afficher le nombre de points disponible
    print("Le nombre de points disponible est {0}".format(nombre_points))
	
    return nombre_points
```
Si votre programme a été correctement écrit, vous devriez voire une simulation visuelle du nombre complexe avant et apres rotation:
<p align="center">
     <img src="img/complexe.PNG?raw=true"/>
</p>
