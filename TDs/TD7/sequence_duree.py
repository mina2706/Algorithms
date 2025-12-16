"""
    Titre : <Séquence de durées>
    Énoncé : <
        On considère une séquence de durées représentée dans un fichier. Ecrire un algorithme qui calcule
        et affiche la durée moyenne des durées de la séquence.
        Le type Durée est défini comme suit dans le lexique partagé :
        Durée : type agrégat
            h : entier >= 0 ; // heures
            m, s : entiers entre 0 et 59 // minutes et secondes
        fagrégat>
    Date   : 16-12-2025
"""
from utils import Durée, dureeEnSecondes, secondesEnDuree

def calculer_duree_moyenne(durees):
    total_secondes = sum(dureeEnSecondes(d) for d in durees) # Calculer le total des durées en secondes
    moyenne_secondes = total_secondes // len(durees) # Calculer la moyenne en secondes
    return secondesEnDuree(moyenne_secondes)

def main():
    durees = [
        Durée(1, 30, 45),
        Durée(2, 15, 30),
        Durée(0, 45, 15)
    ]
    moyenne = calculer_duree_moyenne(durees)
    print(f"La durée moyenne est : {moyenne.h} heures, {moyenne.m} minutes et {moyenne.s} secondes")

if __name__ == "__main__":
    main()