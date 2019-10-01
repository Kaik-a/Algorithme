# algorithme qui permet de trouver le plus grand dénominateur commun PGCD entre deux nombres selon \
# l'algorithme d'Euclide


def gcd(a, b):
    while b != 0:  # jusqu'à ce que le reste soit 0
        t = a  # on affecte a à une variale temporaire t
        a = b  # on affecte b à a
        b = t % b  # on fait la division de t par b et le reste devient b

    return a


print(gcd(360, 252))
print(gcd(20, 8))
