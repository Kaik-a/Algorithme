"""Création d'un algorithme de tri fusion"""

tabl = [12, 0, 74, 5, 17, 20, 1]


def mergesort(tab):
    if len(tab) > 1:  # si la taille du tableau est supérieure à 1
        x = len(tab) // 2  # On divise le tableau en deux
        lefttab = tab[:x]  # On créé deux tableaux à partir du premier
        righttab = tab[x:]

        mergesort(lefttab)  # on applique le début récursivement sur chacune des parties jusqu'a ce que les tableaux
        # fassent len 1
        mergesort(righttab)

        i = 0
        j = 0
        k = 0

        while i < len(lefttab) and j < len(righttab):  # On récupère les éléments en les comparant deux à deux et en les
            # intégrant dans un tableau merged
            if lefttab[i] < righttab[j]:
                tab[k] = lefttab[i]
                i += 1
            else:
                tab[k] = righttab[j]
                j += 1
            k += 1

        while i < len(lefttab):  # On récupère s'il reste des éléments dans lefttab
            tab[k] = lefttab[i]
            i += 1
            k += 1

        while j < len(righttab):  # On récupère s'il reste des éléments dans righttab
            tab[k] = righttab[j]
            j += 1
            k += 1


print(tabl)
mergesort(tabl)
print(tabl)