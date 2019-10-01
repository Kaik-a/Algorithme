dic = {"key1": 1, "key2": 2, 3: "key3"}
key = "k"
for v in dic.items():
    """si un seul argument pris, retrour clé + valeur"""
    print("la clé est: " + str(key) + " et la valeur est: " + str(v))

for cle, valeur in dic.items():
    """fait la distinction entre clé et valeur dans l'ordre ci-dessus"""
    print("la clé est: " + str(cle) + " et la valeur est: " + str(valeur))


def decompte(x):
    """recursion"""
    if x == 0:
        print("done")
    else:
        print(str(x) + "...")
        decompte(x - 1)


decompte(5)


def power(num, pwr):
    """mettre un nombre à une puissance donnée"""
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    """trouver le factoriel d'un nombre"""
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(8))  # 8*7*6*5*4*3*2*1

print(power(5, 3))  # 5*5*5 


