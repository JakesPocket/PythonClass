'''
Project Name: P2 - Turtle Patterns I
Author:Jake McBride
Due Date: 2021-10-03
Course: CS1400-602

Description:
This program draws a picture using the Turtle module.

New things I've learned:
    -Loops (for,while)
    -Iteration
    -Lists (append,insert,pop,remove)

ReadMe:
    Program runs best at 1200 width and 1000 height.

'''
import turtle
import random



def main():
    '''
    Program starts here.
    '''


    try:
        width = input('Please, enter the screen width:')
        width = int(width)

        height = input('Please, enter the screen height:')
        height = int(height)
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return

    BG_COLOR = 'midnight blue'
    #create object 't' from turtle class and initiate
    t = turtle.Turtle()
    t.speed(11)

    #create object 's' and initiate
    s = turtle.Screen()
    s.bgcolor(BG_COLOR)
    s.setup(width, height)

    
    #draw stars in the 'night sky'
    draw_star(t, -520,   20, 20, 'random')
    draw_star(t, -462,  -30, 40, 'random')
    draw_star(t, -145,  -85, 75,    'white')
    draw_star(t, -200,   87, 30, 'random')
    draw_star(t, -290,  276, 45, 'random')
    draw_star(t, -500,  364, 30,    'orange')
    draw_star(t, -300,  410, 20, 'random')
    draw_star(t, -180,  412, 35, 'random')
    draw_star(t,  -75,  382, 25,    'white')
    draw_star(t,  170,  375, 40, 'random')
    draw_star(t,  250,  275, 50,    'yellow')
    

    #draw.... (pause for effect)  ...THE MOON!!!
    draw_moon(t, 500, 350, 75, 'yellow', BG_COLOR)
    

    #draw_house(args) # 8 - 10 houses along the center-bottom area to bottom-right corner
    draw_house(t, 100, -350, 'tan', '#662222', .75)
    draw_house(t, -100, -320, 'tomato', '#662222', .5)
    draw_house(t, -250, -400, 'blue', '#662222', 1)
    draw_house(t, 200, -450, 'sky blue', '#662222', 1.5)
    

    #keeps screen window open until closed manually or clicked inside the scene.
    s.exitonclick()




#end - main



#-----------------------------------------------------------------------------------------------#
#--------------------------------Objects (made with atomic shapes)------------------------------#
#-----------------------------------------------------------------------------------------------#
def draw_moon(t, x, y, radius, fill, shadow):
    '''
    Draws a moon with...
        t - the turtle object.
        x and y - screen coordinates.
        radius -  size of the moon.
        fill - color of the moon.
        shadow - color of the shadow.
    '''

    # init turtle
    t.up()
    if x or y != 0:
        t.goto(x, y)

    t.seth(120)
    

    #draw the moon - (with pen kept 'up' and does not show pen lines. Only fill colors)
    t.fillcolor(fill)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.fillcolor(shadow)
    t.begin_fill()
    t.circle(radius - (radius * .33))
    t.end_fill()
    
    
    #reset turtle
    t.seth(0)
#end - draw_moon


def draw_star(t, x, y, radius, star_color):
    '''
    Draws a moon with...
        t - the turtle object.
        x and y - screen coordinates.
        radius -  size of the outer circle of the star.
        color - color of the star.
    '''
    star_colors = ['orange', 'yellow', 'white']
    
    #choose random color
    if star_color == 'random':
        star_color = random.choice(star_colors)
    #end - if color is random

    #setup color options
    if star_color == 'orange':
        fill_color = ['#331c00', '#7f4700', '#cc7100', '#ff8e00']
    elif star_color == 'yellow':
        fill_color = ['#333300', '#555500', '#cccc00', '#ffff00']
    elif star_color == 'white':
        fill_color = ['#333333', '#555555', '#cccccc', '#ffffff']
    #end - color setup

    # init turtle
    t.up()
    if x or y != 0:
        t.goto(x, y)

    t.seth(0)


    #draw the star - (with pen kept 'up' and does not show pen lines. Only fill colors)
    quarter_radius = radius * .25
    for colors in fill_color:
        t.fillcolor(colors)
        t.pencolor(colors)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        radius -= (quarter_radius)
        t.lt(90)
        t.forward(quarter_radius)  
        t.right(90)
    #end - for loop

    #reset turtle
    t.seth(0)
# end - draw_star


def draw_house(t, x, y, wall_color, roof_color, scale = 1, pen = "black"):
    '''
    Draws a house with...
        t - the turtle object.
        x and y - screen coordinates.
        wall_color - sets color for 'bottom rectangle', 'front parallelogram', and 'front triangle'.
        roof_color - sets color of 'roof parallelogram'.
        scale - sets the scale of the house object (size * scale).
        pen - color of the shape borders
    '''

    # init turtle
    t.up()
    if x or y != 0:
        t.goto(x, y)

    t.seth(0)
    t.pencolor(pen)
    t.down()


    side_base = 100 * scale
    front_base = 96 * scale
    wall_height = 75 * scale
    roof_height = 50 * scale

    slant_length = (roof_height ** 2 + (front_base/2) ** 2 / 4) ** 0.5

    draw_rec(t, x, y, side_base, wall_height, wall_color, 0)

    #move to top-left of 'bottom rectangle' and draw 'roof parallelogram'
    t.up()
    y2 = y + wall_height
    t.down()
    draw_par(t, x, y2, side_base, slant_length, roof_color)

    #move to top-right of 'roof parallelogram' and draw 'front triangle'
    t.up()
    t.seth(0)
    x2 = x + side_base
    draw_tri(t, x2, y2, front_base, wall_color, 'brown', 0, 'iso_tri', slant_length, 150)


    draw_rec(t, 0, 0, wall_height, front_base, wall_color, 270)

    #reset turtle
    t.up()
    t.seth(0)
#end - draw_house

    

#-------------------------------------------------#
#-----------------atomic shapes-------------------#
#-------------------------------------------------#
def draw_tri(t, x, y, side1, fill, pen, tilt = 0, tri_type = 'iso_tri', side2 = None, angle = None):
    '''
    Draws a triangle...
        t - the turtle object.
        x and y - screen coordinates.
        side1 -  length for 2 or 3 sides.
        pen - sets pencolor.
        fill - fill-color of the rectangle.
        tilt - sets the direction of the turtle.
        tri_type - sets Isosolese triangle (iso_tri) or equalateral triangle (equ_tri).
        side2 - in case of type iso_tri.
        angle - also in case of iso_tri.
    '''
    # init turtle
    t.up()
    if x or y != 0:
        t.goto(x, y)
    t.seth(0)
    t.down()
    t.fillcolor(fill)

    t.begin_fill()
    if tri_type == 'iso_tri':
        t.forward(side1)
        t.lt(angle)
        t.forward(side2)
        t.lt(720 - angle * 2)
        t.forward(side2)
    elif tri_type == 'equ_tri':
        for i in range(3):
            t.forward(side1)
            t.lt(60)
    #end - if tri_type
    t.end_fill()


    #reset turtle
    t.up()
    t.seth(0)
#end - draw_tri


def draw_rec(t, x, y, side1, side2, fill, tilt = 0):
    '''
    Draws a recangle...
        t - the turtle object
        x and y - screen coordinates
        side1 and side2 -  lengths for width and heigth, respectively
        fill - fill-color of the rectangle
        tilt - direction of the  turtle     
    '''
   # init turtle
    if x or y != 0:
        t.goto(x, y)

    t.seth(tilt)
    t.down()
    
    t.fillcolor(fill)
    t.begin_fill()
    for i in range(2):
        t.forward(side1)
        t.left(90)
        t.forward(side2)
        t.left(90)
    t.end_fill()

    #reset turtle
    t.up()
    t.seth(0)
#end - draw_rec
 

def draw_par(t, x, y, side1, side2, fill, tilt = 0):
    '''
    Draws a parallelogram...
        t - the turtle object.
        x and y - screen coordinates.
        side1 and side2 -  lengths for width and height, respectively.
        fill - fill-color of the rectangle.
        tilt - sets the direction of the turtle.   
    '''
    # init turtle
    if x or y != 0:
        t.goto(x, y)
    t.seth(tilt)
    t.down()


    #draw rhombus
    t.fillcolor(fill)
    t.begin_fill()
    for i in range(2):
        t.forward(side1)
        t.lt(30)
        t.forward(side2)
        t.lt(150)
    t.end_fill()




    #reset turtle
    t.up()
    t.seth(0)
#end - draw_par



if __name__ == '__main__':
    main()
