chaine = "1, 2, 3, 5, 9, 12, -6, 3, 2, 101, 0, 5"
def lire_csv(input_csv : str) -> list[list] :
    retour = [[],[]]
    for element in input_csv :
        if element==',' or element==' '  :
            continue
        else :
            conversion = int(element)
            if len(retour[0])<0:
                retour[0].append(conversion)
            else:
                retour[1].append(conversion)
    return retour
lire_csv(chaine)