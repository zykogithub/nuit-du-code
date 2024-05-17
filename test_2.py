# question 1
chaine = "1, 2, 3, 5, 9, 12, -6, 3, 2, 101, 0, 5"
def lire_csv(input_csv : str) -> list[list] :
    retour = [[],[]]
    
    return retour
lire_csv(chaine)

# question 2
listeDoublon = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]
def tri_unique(liste : list) -> list :
    rendreUnique : set = set(liste)
    nouvelleListe : list = list(rendreUnique)
    nouvelleListe.sort()
    return nouvelleListe
listeDoublon=tri_unique(listeDoublon)
print(listeDoublon)
'''Créez la classe Cercle, qui doit avoir comme attributs un rayon (un réel) et un centre (un tuple de réels), et implémente les méthodes suivantes :

    getRayon() renvoie le rayon
    getCentre() renvoie les coordonnées du centre
    perimetre() calcule et renvoie le périmètre du cercle
    surface() renvoie la surface du cercle
    '''
from math import*
class Cercle :
    def __init__(self, centre : tuple,  rayon : float) -> None:
        self.rayon = rayon
        self.centre = centre
    def getRayon(self) -> float :
        return self.rayon
    def getCentre(self) -> tuple :
        return self.centre
    def perimetre(self) -> float :
        return 2*pi*self.rayon
    def surface(self) -> float :
        return pi*self.rayon**2
cercle = Cercle((-1,1), 5)
print("Le centre du cercle est :", cercle.getCentre())
print("Son rayon est :", cercle.getRayon())
print(f"Il a pour perimetre {cercle.perimetre()} et pour surface {cercle.surface()}")
# question 4
class Disque :
    def __init__(self, centre : tuple,  rayon : float) -> None:
        self.rayon = rayon
        self.centre = centre
    def getRayon(self) -> float :
        return self.rayon
    def getCentre(self) -> tuple :
        return self.centre
    def intercepte(self,autre_disque) -> bool:
        if self.centre[0]==autre_disque.centre[0] and self.centre[1]==autre_disque.centre[1] :
            return True
        else :
            distance = sqrt(pow(self.centre[0]-autre_disque.centre[0],2)+pow(self.centre[1]-autre_disque.centre[1],2))
            plusPetit = float(abs(self.rayon-autre_disque.rayon))
            plusGrand = float(self.rayon + autre_disque.rayon)
            return True if plusPetit<=distance<=plusGrand else False
d1 = Disque((0,0), 2)
print("Le centre du disque 1 est :", d1.getCentre())
print("Son rayon est :", d1.getRayon())
d2 = Disque((0,0), 1)
print("Le centre du disque 2 est :", d2.getCentre())
print("Son rayon est :", d2.getRayon())
if d1.intercepte(d2):
    print("Le disque 1 intercepte le disque 2")
else:
    print("Le disque 1 n'intercepte pas le disque 2")
# question 5
class Wagon:
    def __init__(self, contenu):
        "Constructeur"
        self.contenu = contenu
        self.suivant = None

    def __repr__(self):
        "Affichage dans la console"
        return f'Wagon de {self.contenu}'

    def __str__(self):
        "Conversion en string"
        return self.__repr__()
class Train:
    def __init__(self):
        "Constructeur"
        self.premier = None
        self.nb_wagons = 0

    def est_vide(self):
        """renvoie True si ce train est vide (ne comporte aucun wagon),
        False sinon
        """
        return True if self.nb_wagons==0 else False

    def donne_nb_wagons(self):
        "Renvoie le nombre de wagons de ce train"
        return self.nb_wagons

    def transporte_du(self, contenu):
        """Détermine si ce train transporte du {contenu} (une chaine de caractères).
        Renvoie True si c'est le cas, False sinon
        """
        wagon : Wagon = self.premier
        while wagon is not None:
            if wagon.contenu == contenu:
                return True
            wagon = wagon.suivant
        return False

    def ajoute_wagon(self, nouveau : Wagon):
        """Ajoute un wagon à la fin de ce train.
        L'argument est le wagon à ajouter
        """
        if self.est_vide():
            self.premier = nouveau
        else:
            wagon : Wagon = self.premier
            while wagon.suivant is not None:
                wagon = wagon.suivant
            wagon.suivant = nouveau
        self.nb_wagons+=1


    def supprime_wagon_de(self, contenu):
        """Supprime le premier wagon de {contenu}
        Renvoie False si ce train ne contient pas de {contenu},
        True si la suppression est effectuée
        """
        # On parcourt le train afin de trouver le contenu
        precedent = None
        wagon = self.premier
        while wagon is not None and wagon.contenu != contenu:
            precedent = wagon
            wagon = wagon.suivant

        if wagon is None:  # on a parcouru tout le train sans trouver le contenu
            return False
        if precedent is None:  # le wagon supprimé est le premier du train
            self.premier = wagon.suivant
        else:  # le wagon supprimé n'est pas le premier
            precedent.suivant = wagon.suivant
        self.nb_wagons -= 1
        return True

    def __repr__(self):
        "Affichage dans la console"
        contenus_wagons = ['']
        wagon = self.premier
        while wagon is not None:
            contenus_wagons.append(str(wagon))
            wagon = wagon.suivant
        return "Locomotive" + " - ".join(contenus_wagons)

    def __str__(self):
        "Conversion en string"
        return self.__repr__()
train = Train()
w1 = Wagon("blé")
train.ajoute_wagon(w1)
w2 = Wagon("riz")
train.ajoute_wagon(w2)
train.ajoute_wagon(Wagon("sable"))
assert str(train) == 'Locomotive - Wagon de blé - Wagon de riz - Wagon de sable'
assert train.est_vide() is False
assert train.donne_nb_wagons() == 3
assert train.transporte_du('blé') is True
assert train.transporte_du('matériel') is False
assert train.supprime_wagon_de('riz') is True
assert str(train) == 'Locomotive - Wagon de blé - Wagon de sable'
train.ajoute_wagon(w2)
assert train.supprime_wagon_de('blé') is True
assert str(train) == 'Locomotive - Wagon de sable - Wagon de riz'
assert train.supprime_wagon_de('blé') is False
