
#Exo 1: 

def initTable():
    liste=[]
    for i in range(1,11):
        liste.append(list(range(0,11*i,i)))
    return liste

print(initTable())

#Exo 2:
def fact (n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

#Exo 3:
def init (n):
    liste=[]
    for i in range(0,n):
        liste.append(0)
    return liste

#Exo 4:
def rechercheMax (liste):
    pge=liste[0]
    for i in liste:
        if (i>pge):
            pge=i
    return pge

#Exo 5
def moyenne(liste):
    somme=0
    for i in liste:
        somme+=i
    return somme/len(liste)

print(moyenne([5,7,2,8]))

#Exo 6
def contain(liste, elem):
    for i in liste:
        if i == elem:
            return True
    return False

#Recursif

