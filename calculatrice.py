def addition(nbr1, nbr2):
    return nbr1 + nbr2

def soustraction(nbr1, nbr2):
    return nbr1 - nbr2

def multiplication(nbr1, nbr2):
    return nbr1 * nbr2

def division(nbr1, nbr2):
    if nbr2 == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    else:
        resultat = nbr1 / nbr2
        return round(resultat, 3)

print("Choisissez l'opération que vous souhaitez effectuer :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
print("5. Quitter")

while True:
    choix = input("Faites votre choix : ")

    if choix == '5':
        print("Bye!")
        break

    while True:
        try:
            nbr1 = float(input("Entrez le premier nombre : "))
            nbr2 = float(input("Entrez le second nombre : "))
            break
        except ValueError:
            print("Vous avez saisi autre chose qu'un nombre.")

    if choix == '1':
        print("Résultat :", addition(nbr1, nbr2))
    elif choix == '2':
        print("Résultat :", soustraction(nbr1, nbr2))
    elif choix == '3':
        print("Résultat :", multiplication(nbr1, nbr2))
    elif choix == '4':
        try:
            print("Résultat :", division(nbr1, nbr2))
        except ZeroDivisionError as e:
            print("Erreur :", e)
    else:
        print("Ce choix est invalide")
