import enum
import random

class Etat(enum.Enum):
     EnVie = 2
     EnFeu = 1
     EnCendre = 0

class Arbre:

    def __init__(self):
        self.__etat = Etat.EnVie

    def brule(self):
        if (self.__etat == Etat.EnVie):
            self.__etat = Etat.EnFeu

    def crame(self):
        if (self.__etat == Etat.EnFeu):
            self.__etat = Etat.EnCendre

    def getEtat(self):
        return self.__etat

    def __str__(self):
        if (self.__etat == Etat.EnFeu):
            return "*"
        elif (self.__etat == Etat.EnCendre):
            return "#"


class Bouleau(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        if (self.getEtat() == Etat.EnVie):
            return "B"
        else :
            return super().__str__()
    
    def propage(self, foret, i, j):
        if (foret[i][j].getEtat()==Etat.EnFeu):
            foret[i][j].crame()
            if (i>0 and j>0):
                foret[i-1][j-1].brule()
            if (i>0):
                foret[i-1][j].brule()
            if (i>0 and j<len(foret)):
                foret[i-1][j+1].brule()
            if (j>0):
                foret[i][j-1].brule()
            if (j<len(foret)):
                foret[i][j+1].brule()
            if (i<len(foret) and j>0):
                foret[i+1][j-1].brule()
            if (i<len(foret)):
                foret[i+1][j].brule()
            if (i<len(foret) and j<len(foret)):
                foret[i+1][j+1].brule()

class Chene(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        if (self.getEtat() == Etat.EnVie):
            return "C"
        else :
            return super().__str__()

    def propage(self, foret, i, j):
        if (foret[i][j].getEtat()==Etat.EnFeu):
            foret[i][j].crame()
            if (i>0):
                foret[i-1][j].brule()
            if (j>0):
                foret[i][j-1].brule()
            if (j<len(foret)):
                foret[i][j+1].brule()
            if (i<len(foret)):
                foret[i+1][j].brule()


class Sapin(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        if (self.getEtat() == Etat.EnVie):
            return "S"
        else :
            return super().__str__()

    def propage(self,foret, i, j):
        if (foret[i][j].getEtat()==Etat.EnFeu):
            foret[i][j].crame()
            if (i>0 and random.randint(0,1)==1):
                foret[i-1][j].brule()
            if (j>0 and random.randint(0,1)==1):
                foret[i][j-1].brule()
            if (j<len(foret) and random.randint(0,1)==1):
                foret[i][j+1].brule()
            if (i<len(foret) and random.randint(0,1)==1):
                foret[i+1][j].brule()

class Vide(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        if (self.getEtat() == Etat.EnVie):
            return " "
        else :
            return super().__str__()

    def propage(self, foret, i, j):
        pass

class Foret:

    def __init__(self, pBouleau, pSapin, pChene, taille):
        self.arbres = []
        for i in range (0,taille):
            self.arbres.append([])
            for j in range (0,taille):
                alea = random.randint(0,100)
                if alea < pBouleau:
                    self.arbres[i].append(Bouleau())
                elif alea < pBouleau+pChene:
                    self.arbres[i].append(Chene())
                elif alea < pBouleau+pChene + pSapin:
                    self.arbres[i].append(Sapin())
                else:
                    self.arbres[i].append(Vide())

    def propage(self):
        copy = self.arbres
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                self.arbres[i][j].propage(copy,i,j)
        self.arbres = copy

    def encoreEnFeu(self):
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                if (self.arbres[i][j].getEtat()==Etat.EnFeu):
                    return True
        return False

    def allumeLeFeu(self,pos):
        self.arbres[pos][pos].brule()

    def __str__(self):
        ch = ""
        for i in range (0, len(self.arbres)):
            for j in range (0, len(self.arbres)):
                ch += str(self.arbres[i][j]) + " "
            ch += "\n"
        return ch


    
class Simulation:

    def run():
        f = Foret(20,20,20,20)
        f.allumeLeFeu(10)
        while(f.encoreEnFeu()):
            f.propage()
            print(f)

Simulation.run()
