"""
    Titre : <Chaîne binaire>
    Énoncé : <Écrire une action récursive qui affiche la chaîne correspondant à la représentation binaire d'un entier. Pour
            l'affichage on utilisera l'action afficherCar qui affiche un caractère (cf. cours). Spécification de l’action à
            réaliser :
            action écrireChBinaire (consulté x : entier ³ 0, modifié e : écran)
                // Effet : affiche sur l’écran e la chaîne binaire représentant le nombre X, caractère par caractère
            Exemples : écrireChBinaire(12,e) a pour effet d'afficher "1100"
            écrireChBinaire(0,e) a pour effet d'afficher "0"
            écrireChBinaire(126,e) a pour effet d'afficher "1111110">
    Date   : 08-12-2025
"""
def ecrireChBinaire(x):
    if x == 1 or x == 0:
        print (x , end = " ")
    else : #x>1
        ecrireChBinaire(x//2)
        print(x%2 , end =" ")

def main():
    x = int (input("Entrez un entier : "))
    ecrireChBinaire(x)

if __name__ == "__main__":
    main()