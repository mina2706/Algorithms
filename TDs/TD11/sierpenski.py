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
from interface_machine_trace.machine_trace import creer_fenetre_algo
from .utils import traceTriangleEquilat
def sierpinski(m, n, lg):
    traceTriangleEquilat(lg , m)
    if n > 1:
        sierpinski(m, n - 1, lg / 2)
        m.forward(lg / 2)
        sierpinski(m, n - 1, lg / 2)
        m.left(120)
        m.forward(lg / 2)
        m.right(120)
        sierpinski(m, n - 1, lg / 2)
        m.left(60)
        m.backward(lg / 2)
        m.right(60)      



if __name__ == "__main__":
    creer_fenetre_algo(sierpinski, params={'n': '','lg':''})
