import turtle
def draw_square(x,y,len):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(len)
        turtle.left(90)

def draw_line(x1,y1, x2,y2):
    turtle.penup()
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.setpos(x2,y2)    

def draw_figure_lower_left(xc,yc,len):
    turtle.penup()
    turtle.setpos(xc,yc)
    turtle.pendown()
    for x in range(xc,xc+len+1, 20):
        y = yc+len - x
        draw_line(x,xc, yc, y)


l=400
minx=-200
miny=-200
maxx=200
maxy=200
turtle.speed(0)
draw_square(minx,miny,l)
draw_figure_lower_left(minx,miny,int(l/2))
# draw_figure_lower_right(maxx,miny,l/2)
# draw_figure_upper_left(minx,maxy,l/2)
# draw_figure_upper_right(maxx,maxy,l/2)

turtle.mainloop()
