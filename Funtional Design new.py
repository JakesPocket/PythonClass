import turtle

def main():
    turtle.speed(0)
    draw_rec(0, 0, 100, 100)
    draw_rec(40, 0, 20, 40)
    draw_rec(10, 50, 20, 20)
    draw_rec(70, 50, 20, 20)
    draw_tri(100, 100, 100)    
    turtle.mainloop()
    
def set_loc(x, y):
    # Move the turtle to location coordinates int(x) and int(y) and point turtle to the right
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    
def draw_rec(x, y, w, h):
    # Draw a rectangle with width int(w) and height int(h) at location x, y
    set_loc(x, y)
    for i in range(2):
        turtle.forward(w)
        turtle.lt(90)
        turtle.forward(h)
        turtle.lt(90)
  
def draw_tri(x, y, s):
    # Draw a triangle with equal sides of length int(s) at location x, y
    set_loc(x, y)
    for i in range(3):
        turtle.lt(120)
        turtle.forward(s)

if __name__ == '__main__':
    main()

