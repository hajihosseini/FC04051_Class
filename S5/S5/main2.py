import turtle

def draw_line(x1,y1, x2,y2):
    turtle.penup()
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.setpos(x2,y2)
    

turtle.pensize(2)
turtle.speed(0)

for x in range(0,501, 50):
    y = 500 - x
    draw_line(x,0, 0,y)

turtle.mainloop()