import turtle 
def traceCarre2 (lg , t):   
    for _ in range(4):
        t.forward(lg)
        t.left(90)

def traceTriangleEquilat (lg , t):
    for _ in range(3):
        t.forward(lg)
        t.left(120)

def machine_config():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    return screen, t

def save_drawing(screen, filename):
    canvas = screen.getcanvas()
    path = "/workspaces/Algorithms/TDs/rendus_machine_tarce/"
    canvas.postscript(file= f"{path}{filename}")
    print("Dessiné :", f"{path}{filename}")