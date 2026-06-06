
# reduce prend une fonciton et une liste :
    # applique la fonction sur les deux premiers elements 
    # puis le res et l'element suivant 
    # etc etc 


from functools import reduce 


mots = ["connexion", "réussie", "bienvenue", "luna"]

phrase = reduce(lambda a,b: a + " " + b, mots)

print(mots)
print(phrase)

