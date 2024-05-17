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
        