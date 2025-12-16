"""
    Titre : < Racine carrée>
    Énoncé : <
        Ecrire la fonction Racine qui calcule la racine carrée d'un réel X par la méthode de Newton : on considère la
        suite a définie par récurrence :
            a0 = X/2
            ai+1 = (ai + X/ai) / 2
        Le résultat est an tel que : | (an+1 - an) / an | £ e, pour e = 10-6.
        fonction Racine(X : réel>= 0) -> réel >= 0
            { Racine(X) désigne la racine carrée de X }
        Exemple : Pour le calcul de Racine(9) on a :
            a0 = 4.5, a1 = (4.5 + 9/4.5) /2 = 3.25, a2 = (3.25 + 9/3.25) /2 = 3.00961
            a4 = 3.0000153, a5 = 3, a6 = 3
        >
    Date   : 16-12-2025
"""
import math
def racine(X , e):
    res = X / 2.0
    erreur = 1
    while erreur > e:
        prochain = (res + X / res) / 2.0
        erreur = abs((prochain - res) / res)
        res = prochain
    return res
   
def main():
    x = float(input("Entrez un nombre réel positif pour calculer sa racine carrée : "))
    e = 1e-6
    if x < 0:
        print("Veuillez entrer un nombre réel positif.")
    else:
        resultat = racine(x, e)
        print(f"La racine carrée de {x} est approximativement {resultat}.")
if __name__ == "__main__":
    main()