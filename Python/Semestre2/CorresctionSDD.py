
class Pile:

  def __init__(self):
    self.valeurs = []

  def ajoute(self, valeur):
     self.valeurs.insert(0, valeur)#append()

  def retire(self):
    if self.valeurs:
        return self.valeurs.pop() #pop(0)

  def estVide(self):
    return self.valeurs == []

  def taille(self):
      return len(self.valeurs)
      
  def __str__(self):
    ch = ''
    for x in self.valeurs:
        ch = " | " + str(x) + ch
    return ch +" |"
    
p = Pile()
p.ajoute(9)
p.ajoute(2)
p.ajoute(5)

print(p.taille())

p.retire()
p.ajoute(7)

print(p.estVide())


##########################################
dico = {"Jeu":"Game", "Joueur":"Player", "Tester":"Test"}

dico["Nouveau"]="New" 


def ajouter (mot,trad,dico):
    if not mot in dico.keys():
        dico[mot]=trad

ajouter("Etudiant","Student",dico)

def listeTrad(dico):    
    for cle in dico.keys():
      print(dico[cle])
      
def supprime(char,dico):
    aSuppr =  []
    for cle in dico.keys():
        if (cle[0]==char):
            aSuppr.append(cle)
    for i in aSuppr:
        del dico[i]
        
supprime ("J", dico)

for cle,valeur in dico.items():
      print(cle + " "+ valeur)

