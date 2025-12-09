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

def lesCarres(n, lg , d, t):
    traceCarre2(lg,t)
    if lg>d and n>0 : # si n=0 y a que le carré de base , donc pas de carrés emboités
        lesCarres(n-1, lg-d, d , t) 

def main ():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    n = int (input ("Entrez le nombre de carrés emboités : "))
    lg = int (input ("Entrez le coté de carré de base : "))
    d = int (input("Entrez la différence entre les carrés emboités : "))
    lesCarres(n, lg ,d , t)

    # enregistrer le canevas en PostScript
    canvas = screen.getcanvas()
    out = "/workspaces/Algorithms/TDs/rendus_machine_tarce/carres_emboites.ps"
    canvas.postscript(file=out)
    print("Dessiné :", out)

    screen.bye()

if __name__ == "__main__":
    main()