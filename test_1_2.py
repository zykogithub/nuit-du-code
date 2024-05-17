from math import *
from pprint import *
from typing import Any
'''
x : int = 4
y : float = 1.2
t : int = "aba"

monentier=0

n=0

maliste = [i+1 for i in range(10)]

felins = maliste[:3]

x = len(maliste)

if "chat" in maliste:
        print("miaou")
elif "chat" not in maliste and "chien" in maliste :
        print("ouaf")
if 1<= monentier <= 5 :
    print("petit")
if 6<= monentier <= 10 :
    print("grand")
    
for i in range(n):
    print(f"*"*n)

i=1
n = 10
while n!=1 :
    i+=1
    if n%2==0 :
        n=n//2
    else :
        n=n*3+1

delta = lambda a,b,c : b**2-4*a*c

def racine_2d(a,b,c) :
    delta = b**2-4*a*c
    deltaPositif = delta>=0
    deltaNul = delta==0
    if deltaPositif and not deltaNul :
        return (-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a)
    elif deltaPositif and deltaNul :
        return -b/(2*a),-b/(2*a)
    else :
        return None,None
import pprint

from math import *

def racine_2d(a,b,c) :
    delta = b**2-4*a*c
    deltaPositif = delta>=0
    deltaNul = delta==0
    if deltaPositif and not deltaNul :
        return (-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a)
    elif deltaPositif and deltaNul :
        return -b/(2*a),-b/(2*a)
    else :
        return None,None
        
        
        
class Fruit :
    def __init__(self) -> None:
        self.__mass : int = 100
    def __str__(self) -> str:
        return f"classe mère : {self.__mass}\n"
    def get_masse (self) :
        return self.__mass
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
class Citron(Fruit) :
    def __init__(self) -> None:
        super().__init__()
        self.__mass = 200
    def __str__(self) -> str:
        return super().__str__() + f"classe fille : {self.__mass}"
if __name__ == "__main__" :
    citron1 = Citron()
    print(citron1)
    print(citron1.__dict__)
    '''
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
        