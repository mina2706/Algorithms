import tkinter as tk
from turtle import RawTurtle, TurtleScreen

def creer_fenetre_algo(algo, params=None, width=600, height=600, canvas_width=1200, canvas_height=1200):
    """
    Fenêtre Turtle avec scrollbars pour grands dessins.
    - algo : fonction (tortue, **params)
    - params : dictionnaire des paramètres
    - width, height : taille visible de la fenêtre
    - canvas_width, canvas_height : taille réelle du canvas scrollable
    """
    if params is None:
        params = {}

    root = tk.Tk()
    root.title("Fenêtre de dessin Turtle avec scroll")

    # --- Frame principale ---
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # --- Canvas avec scrollbars ---
    canvas_frame = tk.Frame(main_frame)
    canvas_frame.pack(side="left", fill="both", expand=True)

    h_scroll = tk.Scrollbar(canvas_frame, orient="horizontal")
    h_scroll.pack(side="bottom", fill="x")

    v_scroll = tk.Scrollbar(canvas_frame, orient="vertical")
    v_scroll.pack(side="right", fill="y")

    canvas = tk.Canvas(canvas_frame, width=width, height=height,
                       scrollregion=(0, 0, canvas_width, canvas_height),
                       xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
    canvas.pack(side="left", fill="both", expand=True)

    h_scroll.config(command=canvas.xview)
    v_scroll.config(command=canvas.yview)

    screen = TurtleScreen(canvas)
    screen.bgcolor("white")
    t = RawTurtle(screen)
    t.speed(0)

    # --- Frame pour paramètres et bouton ---
    control_frame = tk.Frame(main_frame)
    control_frame.pack(side="right", fill="y", padx=10, pady=10)

    tk.Label(control_frame, text="Paramètres").pack()

    entry_widgets = {}
    for key, value in params.items():
        frame = tk.Frame(control_frame)
        frame.pack(pady=2)
        tk.Label(frame, text=f"{key}:").pack(side="left")
        entry = tk.Entry(frame, width=8)
        entry.pack(side="left")
        entry.insert(0, str(value))
        entry_widgets[key] = entry

    def dessiner():
        t.reset()
        param_vals = {k: int(w.get()) for k, w in entry_widgets.items()}
        algo(t, **param_vals)

    tk.Button(control_frame, text="Dessiner", command=dessiner).pack(pady=10)

    root.mainloop()
