from math import *
from pprint import *
from typing import Any

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
n = 1
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

