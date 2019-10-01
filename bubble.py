"""Création d'algorithme de tri à bulles"""

tab = [12, 0, 74, 5, 17, 20, 1]

i = 0

while i < len(tab)-1:
    if tab[i] > tab[i+1]:
        print(tab[i])
        tab[i], tab[i+1] = tab[i+1], tab[i]
        i = 0
    else:
        i = i+1

print(tab)

