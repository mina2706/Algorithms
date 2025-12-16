from machine_trace import creer_fenetre_algo

# --- Votre algorithme ---
def triangle(m, n, taille):
    """
    Dessine n triangles successifs.
    """
    for _ in range(n):
        for _ in range(3):
            m.forward(taille)
            m.left(120)
        m.left(10)  # petite rotation entre les triangles


# --- Appel de la fenêtre ---
creer_fenetre_algo(
    triangle,
    params={
        'n': 3,
        'taille': 100
    }
)
