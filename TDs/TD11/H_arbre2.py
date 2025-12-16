'''
    Version 2 de l'action recursive hArbre en se servant de la symétrie
'''
import turtle
from interface_machine_trace.machine_trace import creer_fenetre_algo

def hArbre2(t, n, lg):
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
            hArbre2(t, n-1, lg/2)
            t.left(90)
            t.backward(lg)
            t.right(90)
            hArbre2(t, n-1, lg/2)
            t.left(90)
            t.forward(lg/2)
            t.left(90)
            t.forward(lg/2)

if __name__ == "__main__":
    creer_fenetre_algo(hArbre2, params={'n': '','lg':''})

