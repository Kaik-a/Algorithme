"""Création d'algorithme de recherche binaire"""

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binary_search(item, itemlist):
    listsize = len(itemlist) - 1
    lower_index = 0
    upper_index = listsize

    # On parcourt la liste tant que l'index inférieur ne dépasse pas l'index supérieur
    while lower_index <= upper_index:
        middle_point = (lower_index + upper_index) // 2  # On définit le milieur de la liste

        if itemlist[middle_point] == item:  # Si le milieur la valeur recherchée on la renvoie
            return middle_point

        if item > itemlist[middle_point]:  # Si le milieu est petit que la valeur on cherche dans la moitié la plus grde
            lower_index = middle_point + 1
        else:  # Sinon on cherche dans la plus petite
            upper_index = middle_point - 1

    if lower_index > upper_index:  # Quand l'index le plus petit dépasse le plus grand cela indique que la valeur
        # n'existe pas dans la liste
        return "il n'est pas là"


print(items)
print(binary_search(10, items))
print(binary_search(19, items))