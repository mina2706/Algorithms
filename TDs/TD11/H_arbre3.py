'''
    Version 2 de l'action recursive hArbre en se servant de la symétrie
    Il trace le H principal au fur et à mesure de la recursion
'''
import turtle
import time
from interface_machine_trace.machine_trace import creer_fenetre_algo

def hArbre3(t, n, lg):
    if n>=1 :
        for _ in range(2):  # répéter pour les deux moitiés la droite puis la gauche
            t.forward(lg/2)
            t.left(90)
            t.forward(lg/2)
            t.right(90)
            hArbre3(t, n-1, lg/2)
            t.left(90)
            t.backward(lg)
            t.right(90)
            hArbre3(t, n-1, lg/2)
            t.left(90)
            t.forward(lg/2)
            t.left(90)
            t.forward(lg/2)

if __name__ == "__main__":
    debut = time.time()
    creer_fenetre_algo(hArbre3, params={'n': '','lg':''})
    fin = time.time()
    print(f"Temps d'exécution : {fin - debut} secondes")
