"""
    Titre : <Triangle de Sierpinski>
    Énoncé : <Écrire l'action récursive sierpinski qui trace à l’ordre n la figure suivante formée de triangles
            équilatéraux :
                action sierpinski(Consultés n : entier > 0, lg : réel > 0, Modifié m : Machine-tracés)
                    // Effet : trace la figure à l’ordre n, à partir de la position courante de la plume (l’un des sommets du triangle
                    // principal) la longueur du côté du triangle principal est lg.
                    // E.I. : pe = basse, pp = s0 l’un des sommets du triangle principal, cap = a0 sens de tracé du premier côté
                    // E.F. : pe = basse, pp = s0 l’un des sommets du triangle principal, cap = a0 sens de tracé du premier côté
            b) Écrire l’algorithme principal qui saisit les caractéristiques de la figure à tracer puis effectue le
            tracé correspondant en appelant l’action sierpinski.>
    Date   : 10-12-2025

"""
import turtle
from utils import traceTriangleEquilat , machine_config, save_drawing
def sierpinski(n, lg, t):
    if n == 1:
        traceTriangleEquilat(lg , t)
    else:
        sierpinski(n - 1, lg / 2, t)
        t.forward(lg / 2)
        sierpinski(n - 1, lg / 2, t)
        t.backward(lg / 2)
        t.left(60)
        t.forward(lg / 2)
        t.right(60)
        sierpinski(n - 1, lg / 2, t)
        t.left(60)
        t.backward(lg / 2)
        t.right(60)
        sierpinski(n - 1, lg / 2, t)      

def main():
    # configurer la machine à tracer
    screen, t = machine_config()

    n = int(input("Entrez l'ordre du triangle de Sierpinski : "))
    lg = int(input("Entrez la longueur du côté du triangle principal : "))

    sierpinski(n, lg, t)

    # enregistrer le canevas en PostScript
    save_drawing(screen, "sierpinski.ps")
    
    screen.bye()

if __name__ == "__main__":
    main()