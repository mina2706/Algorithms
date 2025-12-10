'''
    Version 2 de l'action recursive hArbre en se servant de la symétrie
'''
import turtle
from utils import machine_config, save_drawing

def hArbre2(n, lg, t):
    for _ in range(2):  # répéter pour les deux moitiés la droite puis la gauche
        t.forward(lg/2)
        t.left(90)
        t.forward(lg/2)
        t.backward(lg)
        t.forward(lg/2)
        t.left(90)
        t.forward(lg/2)

    if n>1 :
        for _ in range(2):  # répéter pour les deux moitiés la droite puis la gauche
            t.forward(lg/2)
            t.left(90)
            t.forward(lg/2)
            t.right(90)
            hArbre2(n-1, lg/2, t)
            t.left(90)
            t.backward(lg)
            t.right(90)
            hArbre2(n-1, lg/2, t)
            t.left(90)
            t.forward(lg/2)
            t.left(90)
            t.forward(lg/2)

def main ():
    # configurer la machine à tracer
    screen, t = machine_config()

    n = int (input ("Entrez l'ordre de l'arbre , n  : "))
    lg = int (input ("Entrez la longueur des branches de l'arbre de base , lg : "))
    hArbre2(n, lg , t)

    # enregistrer le canevas en PostScript
    save_drawing(screen, "H_arbre2.ps")
   
    screen.bye()

if __name__ == "__main__":
    main()   