from gettext import find
import pandas as pd


print("pokemon")

abc = pd.read_csv("Pokemon.csv") 

print(abc.columns)
print(abc["Name"])
for pok in abc["Name"]:
    print(pok)

findPokemon = input("is pokemon in list")

print (findPokemon)


#for x in abc["Name"]:
    #if findPokemon == x:
        #print("Yes it's on the list")
    #else:
        #print("not on the list")
    #if findPokemon != x:
        #print("thispokemon is not on the list")
        
def zoekPokemon(zoekterm):
    for voortuin in abc["Name"]:
        if zoekterm == voortuin:
            return True
    return False

zpok = input("Welke Pokemon zoek je? ")

if zoekPokemon(zpok):
    print("yes")
else:
    print("no")