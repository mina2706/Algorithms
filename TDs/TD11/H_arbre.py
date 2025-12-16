"""
    Titre : <H arbre>
    Énoncé : <Écrire l'action récursive hArbres qui trace la figure suivante (un H-Arbre) à l’ordre n à partir de la
            position courante de la plume : 
            action hArbre (Consultés n : entier ≥ 0, lg : réel > 0, Modifié m : machine-tracés)
                // Effet : trace un H-Arbre à l’ordre n, la longueur des branches du H principal est lg
                // E.I. : pe = basse, pp = s0 milieu de la branche horizontale du H principal, cap = a0
                // E.F. : H-Arbre tracé à l’ordre N, pe = basse, pp = s0, cap = a0>
    Date   : 08-12-2025
"""
import turtle
from interface_machine_trace.machine_trace import creer_fenetre_algo
def hArbre(t, n, lg):
    # dessiner le H de base et revenir au centre, cap = droite
    t.backward(lg/2)      # milieu gauche
    t.left(90)
    t.forward(lg/2)       # sommet gauche haut
    t.backward(lg)        # sommet gauche bas
    t.forward(lg/2)       # revenir au milieu gauche
    t.right(90)           # cap = droite
    t.forward(lg)         # aller au milieu droit
    t.left(90)
    t.forward(lg/2)       # sommet droit haut
    t.backward(lg)        # sommet droit bas
    t.forward(lg/2)       # revenir au milieu droit
    t.right(90)           # cap = droite
    t.backward(lg/2)      # revenir au centre

    if n > 1:
        # top-left
        t.backward(lg/2)
        t.left(90)
        t.forward(lg/2)
        t.right(90)           # cap = droite au sommet haut-gauche
        hArbre(t, n-1, lg/2)
        # annuler (inverse des 4 mouvements ci‑dessus)
        t.left(90)
        t.backward(lg/2)
        t.right(90)
        t.forward(lg/2)

        # bottom-left
        t.backward(lg/2)
        t.left(90)
        t.backward(lg/2)
        t.right(90)           # cap = droite au sommet bas-gauche
        hArbre(t, n-1, lg/2)
        t.left(90)
        t.forward(lg/2)
        t.right(90)
        t.forward(lg/2)

        # top-right
        t.forward(lg/2)
        t.left(90)
        t.forward(lg/2)
        t.right(90)           # cap = droite au sommet haut-droit
        hArbre(t, n-1, lg/2)
        t.left(90)
        t.backward(lg/2)
        t.right(90)
        t.backward(lg/2)

        # bottom-right
        t.forward(lg/2)
        t.right(90)
        t.forward(lg/2)
        t.left(90)            # cap = droite au sommet bas-droit
        hArbre(t, n-1, lg/2)
        t.right(90)
        t.backward(lg/2)
        t.left(90)
        t.backward(lg/2)

if __name__ == "__main__":
    creer_fenetre_algo(hArbre, params={'n': '','lg':''})
