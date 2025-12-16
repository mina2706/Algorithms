"""
    Titre : < Le dernier caractère d'une séquence >
    Énoncé : <
            On considère une séquence de caractères représentée dans un fichier. Ecrire un algorithme qui
            affiche la valeur du dernier caractère de la séquence.
        >
    Date   : 16-12-2025
"""
def dernier (sequence):
    if len(sequence) == 0:
        print("La séquence est vide.")
    else:
        return sequence[-1] # les indices négatifs permettent d'accéder aux éléments en partant de la fin

def main():
    sequence = ""
    print("Le dernier caractère est : ", dernier(sequence))

if __name__ == "__main__":
    main()