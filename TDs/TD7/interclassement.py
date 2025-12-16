"""
    Titre : <Interclassement de deux séquences triées>
    Énoncé : <
        On considère deux séquences d'entiers positifs triées en ordre croissant représentées dans des
        fichiers. Un même nombre peut apparaître plusieurs fois dans une séquence. Ecrire un algorithme qui
        réalise l'interclassement des deux séquences : le résultat est un fichier contenant une troisième
        séquence en ordre croissant comportant tous les éléments présents dans les deux séquences lues.
        Si un même élément apparaît x fois dans la première séquence et y fois dans la deuxième, il doit
        apparaître x+y fois dans la séquence résultat. Les séquences lues peuvent être vides.
            Exemple : 
                séquence 1 : 1 1 3 4 11 11 25 28 30 30 32 40
                séquence 2 : 1 2 3 5 5 11 24 25 29
                séquence résultat : 1 1 1 2 3 3 4 5 5 11 11 11 24 25 25 28 29 30 30 32 40
    >
    Date   : 16-12-2025
"""
def interclassement(seq1, seq2):
    if len(seq1) == 0 and len(seq2) == 0:
        print("Les deux séquences sont vides.")
        resultat = []
    else : 
        if len(seq1) == 0: # la 1ere séquence est vide en recopie la 2eme dans le resultat
            resultat = seq2
        if len (seq2) == 0: # la 2eme séquence est vide en recopie la 1ere dans le resultat
            resultat = seq1
        else: # les deux séquences sont non vides
            resultat = []
            i, j = 0, 0 # indices de parcours des deux séquences
            while i<len(seq1) and j<len(seq2): # tant qu'on n'a pas atteint la fin d'une des deux séquences
                if seq1[i] <= seq2[j]: # le plus petit élément est dans la 1ere séquence
                    resultat.append (seq1[i]) # on ajoute le plus petit élément au résultat
                    i += 1 # on avance dans la 1ere séquence
                else: # le plus petit élément est dans la 2eme séquence
                    resultat.append (seq2[j])  # on ajoute le plus petit élément au résultat
                    j += 1 # on avance dans la 2eme séquence
            # on a atteint la fin d'une des deux séquences, on ajoute les éléments rest

            if i == len(seq1): # la 1ere séquence est terminée
                resultat.extend (seq2[j:]) # on ajoute les éléments restants de la 2eme séquence au résultat
            else: # la 2eme séquence est terminée
                resultat.extend (seq1[i:]) # on ajoute les éléments restants de la 1ere séquence au résultat
    return resultat
            
def main():
    seq1 = [1, 1, 3, 4, 11, 11, 25, 28, 30, 30, 32, 40]
    seq2 = [1, 2, 3, 5, 5, 11, 24, 25, 29]
    resultat_prevu = [1, 1, 1, 2, 3, 3, 4, 5, 5, 11, 11, 11, 24, 25, 25, 28, 29, 30, 30, 32, 40]
    print("Séquence résultat : ", interclassement (seq1, seq2))
    if interclassement (seq1, seq2) == resultat_prevu:
        print("Le résultat est correct.")   
    else:
        print("Le résultat est incorrect.")
if __name__ == "__main__":
    main()