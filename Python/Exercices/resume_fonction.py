import random

#Commentaire
"""
Test sur plusieurs lignes
"""

#variable et type
var = random.randint(0,100)
print(var)
a = 5
b = 8.2
c = "Hello"
d = True

print (type(var))

#operateur (type)
print (a+b)
print (a-b)
print (a*b)
print (a**b) #puissance
print (a/b)
print (a//b) #quotient
print (a%b)  #reste (modulo) 

# int +,-,*,/,//,**,% float -> float
# float +,-,*,/,//,**,% float -> float
# int +,-,*,//,**,% int -> int
# int / int -> float

# listes
liste = []
liste = list (range (0,100,5))
liste.append(25) #ajoute 25 à la fin de la liste
len(liste) #donne la taille de la liste

# boucles
for i in liste:
    print(i)

for i in range(0,10):
    print(i)

i=1
while i<100:
    i = i*2
    print(i)

#fonctions
def multiplier (a,b):
    return a * b

# if elif else
if a == 1:
    print ("afficher égal 1")
elif d: #equivaut à d == True
    print ("d est True")
else :
    print("les deux sont faux")