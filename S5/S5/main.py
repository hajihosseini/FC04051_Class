import turtle
import random

def get_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)

def DrawPolygonSpiral(n, l, ld, ad):
    for j in range(90):
        for i in range(n):
            turtle.forward(l)
            a = 360/n            
            turtle.right(a)
        a = a * ad
        l = l * ld
        turtle.right(5)
        c = get_random_color()
        turtle.pencolor(c)

turtle.speed(2)
# turtle.tracer(0)
turtle.pensize(2)
turtle.penup()
turtle.setpos(0, 200)
turtle.pendown()
DrawPolygonSpiral(18, 100, 0.98, 1.02)
# turtle.update()
turtle.mainloop()