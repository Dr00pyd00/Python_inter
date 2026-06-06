

def carre_gen():
    for x in range(10):
        yield x * x


# c'est un objet:
print(carre_gen)

# je peux creer une instance et l'utiliser:
gen = carre_gen()

print(gen) # objet
# lancer le truc:
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# on peut lire avec une for loop:
# for c in carre_gen():
#     print(c)


# on peut utiliser expression generatrice:
print("expression gen:")

my_gen = (x * 10 for x in range(5))

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# print(next(my_gen))   leve erreur StopIteration  car plus rien a chopper



