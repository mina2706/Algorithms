
# README — Utilisation de `creer_fenetre_algo`

## 📌 Prérequis

* Python 3 installé
* Le fichier **machine_trace.py** présent dans le même dossier
* Aucun autre module externe n’est nécessaire (uniquement tkinter et turtle, déjà inclus dans Python)

---

## 🎯 Objectif

`creer_fenetre_algo` permet d’ouvrir automatiquement une **fenêtre graphique** Turtle avec :

* des **champs pour saisir les paramètres**
* un **bouton Dessiner**

Elle sert à tester visuellement n'importe quel algorithme Turtle sans écrire d’interface.

---

## 🧩 Comment l’utiliser dans votre algorithme ?

1. **Écrire votre fonction normalement**, en mettant la machine (tortue) en premier paramètre
   → par convention la machine s’appelle **m**

   Exemple :

   ```python
   def mon_algo(m, a, b):
       ...
   ```

2. **Appeler la fonction** `creer_fenetre_algo` **à la fin du fichier** :

   ```python
   creer_fenetre_algo(mon_algo, params={'a': valeur, 'b': valeur})
   ```

3. **Exécuter le fichier Python**
   → Une fenêtre s'ouvre avec les champs de paramètres.
   → Saisissez les valeurs (ou gardez celles par défaut).
   → Cliquez **Dessiner**.

---

## ✅ Exemple complet à copier-coller

### 📄 Fichier : `triangle.py`

```python
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
```

### ▶️ Exécution

```bash
python triangle.py
```

Une fenêtre s’ouvre :

* champs **n** et **taille** modifiables
* bouton **Dessiner**


---

