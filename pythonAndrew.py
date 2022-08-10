from operator import truediv


print("hoi")
aword = "woordje"
print(aword)
aword = 35
print(aword)

getal = 60
if getal == 60:
    print("getal is 60")
    print("dit is ook 60")

naam = input("What is your name?")

print(naam)

if naam == "andrew":
    print("your name is andrew") #needs indentation for if statements

list = [12, 14, 1, 7, 99]
for x in list:
    print(x)

for y in range(10):
    print(y)
for z in range(4,15):
    print(z)
for a in range(4,15,3):
    print(a)

nummer = 35

print("het nummer is " + str(nummer)) #concastination/cast 
print("het nummer is toch echt", nummer, "some other stuff") #alternative casting

leeftijd = input("wat is je leeftijd")
print(int(leeftijd) + int(10))

def ditgaanwedoen():
    getal = 8
    getal2 = 16
    getal = getal2 + getal
    getal = getal / 4
    print("dit gaan we doen", getal)

ditgaanwedoen()
ditgaanwedoen()

def anderefunctie(myParam):
    print(myParam * myParam)
    return 6 #maandag

go = anderefunctie(5) #argument
anderefunctie(12)
anderefunctie(366)
print(anderefunctie(5))
print(go)

print( anderefunctie(5) + anderefunctie(5))

#proceduaral programming 1947
#object orientated programming 1990
#functional programming/stateless programming 2015 lamda's 
#stream





