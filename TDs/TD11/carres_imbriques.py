"""
    Titre : <Carrés emboîtés>
    Énoncé : <Écrire l'action récursive suivante :
        action lesCarrés (Consultés n : entier ³ 0, lg : réel > 0, d : réel > 0, Modifié m : machine-tracés)
            // Effet : trace la figure d'ordre n, la longueur du côté du carré extérieur est lg, la différence de longueur
            // entre les carrés emboités est d
            // E.I. : pe = basse, pp = position de l'angle inférieur gauche du carré extérieur, cap = 0
            // E.F. : pe = basse, pp = position de l'angle inférieur gauche du carré extérieur, cap = 0>
    Date   : 08-12-2025
"""
import turtle 
from utils import traceCarre2
from machine_trace import creer_fenetre_algo

def lesCarres(m, n, lg , d):
    traceCarre2(lg,m)
    if lg>d and n>0 : # si n=0 y a que le carré de base , donc pas de carrés emboités
        lesCarres(m, n-1, lg-d, d) 


if __name__ == "__main__":
    creer_fenetre_algo(lesCarres, params={'n':4,'lg':300,'d':20})