'''
Project Name: P2 - Turtle Patterns II
Author:Jake McBride
Due Date: 2021-11-13
Course: CS1400-602

Description:
This program draws a picture using the Turtle module. It will also scale the scene and add two alternate versions.

New things I've learned:
    -New algirithms
    -scaling for ojects and scenes

ReadMe:
    Program runs best at 1200 width and 1000 height.

'''
import turtle
import random
import sys


def main():
    '''
    Program starts here.
    '''
    
    width = 1200
    height = 1000


    
    #create object 't' from turtle class and initiate
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(0, 0)
    #create object 's' and initiate
    s = turtle.Screen()
    s.setup(width, height)
    
    try:
        option = sys.argv[1]
    except:     
        ##choose random option
        options = ['normal', 'comet', 'dusk']
        option = random.choice(options)
        print('please< be sure to type in correctly the <filename> and <option>')

    draw_scene(t, s, option, 0, 0, 1)
    draw_scene(t, s, option, -400, -300, .2)
    

    
    

    #keeps screen window open until closed manually or clicked inside the scene.
    s.exitonclick()




#end - main
def draw_scene(t, s, option, x, y, scale):
    '''
    Draws a scene with...
        t - the turtle object.
        option - alternate scene
        x and y - screen coordinates.
        scale = all coordinates and objects scaled multiplied by the int 'scale'
    '''
    #modify accoring to option
    if option == 'normal':
        bg_color = 'midnight blue'
    elif option == 'comet':
        draw_comet(t, -100, 200, 20, 'brown', 'white', 127, 1)
        draw_comet(t, -350, 300, 20, 'brown', 'white', 115, .2)
        draw_comet(t, -260, 100, 20, 'brown', 'white', 124, .5)
        draw_comet(t, -400, 350, 20, 'brown', 'white', 117, 1.5)
        draw_comet(t, -50, 250, 20, 'brown', 'white', 119, 1.2)
        bg_color = 'midnight blue'
    elif option == 'dusk':
        bg_color = 'dark orange3'
    # End - if option
    if scale != 1:
        #make frame
        draw_rec(t, x - 1200/2 * scale, y - 1000/2 * scale, 1200 * scale, 1000 * scale, None, 'white', 0)


    # Set background color
    s.bgcolor(bg_color)
    
    #draw stars in the 'night sky'
    draw_star(t, -520 * scale + x,   20 * scale + y, 20 * scale, 'random')
    draw_star(t, -462 * scale + x,  -30 * scale + y, 40 * scale, 'random')
    draw_star(t, -145 * scale + x,  -85 * scale + y, 75 * scale,    'white')
    draw_star(t, -200 * scale + x,   87 * scale + y, 30 * scale, 'random')
    draw_star(t, -290 * scale + x,  276 * scale + y, 45 * scale, 'random')
    draw_star(t, -500 * scale + x,  364 * scale + y, 30 * scale,    'orange')
    draw_star(t, -300 * scale + x,  410 * scale + y, 20 * scale, 'random')
    draw_star(t, -180 * scale + x,  412 * scale + y, 35 * scale, 'random')
    draw_star(t,  -75 * scale + x,  382 * scale + y, 25 * scale,    'white')
    draw_star(t,  170 * scale + x,  375 * scale + y, 40 * scale, 'random')
    draw_star(t,  250 * scale + x,  275 * scale + y, 50 * scale,    'yellow')
    

    #draw.... (pause for effect)  ...THE MOON!!!
    draw_moon(t, 500 * scale + x, 350 * scale + y, 75 * scale, 'yellow', bg_color)
    

    #draw_house(args) # 8 - 10 houses along the center-bottom area to bottom-right corner
    draw_house(t, 100 * scale + x, -350 * scale + y, 'tan', '#662222', .75 * scale)
    draw_house(t, -100 * scale + x, -320 * scale + y, 'tomato', '#662222', .5 * scale)
    draw_house(t, -250 * scale + x, -400 * scale + y, 'blue', '#662222', 1 * scale)
    draw_house(t, 200 * scale + x, -450 * scale + y, 'sky blue', '#662222', 1.5 * scale)
    


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

    draw_rec(t, x, y, side_base, wall_height, wall_color, None, 0)

    #move to top-left of 'bottom rectangle' and draw 'roof parallelogram'
    t.up()
    y2 = y + wall_height
    t.down()
    draw_par(t, x, y2, side_base, slant_length, roof_color)

    #move to top-right of 'roof parallelogram' and draw 'front triangle'
    t.up()
    t.seth(0)
    x2 = x + side_base
    draw_tri(t, x2, y2, front_base, wall_color, None, 0, 'iso_tri', slant_length, 150)


    draw_rec(t, 0, 0, wall_height, front_base, wall_color, None, 270)

    #reset turtle
    t.up()
    t.seth(0)
#end - draw_house

def draw_comet(t, x, y, width, fill_color, tail_color, tilt, scale):
    '''
    Draws a comet with...
        t - the turtle object.
        x and y - screen coordinates.
        radius -  size of the moon.
        fill - color of the moon.
        tail - color of the tail.
    '''

    # init turtle
    t.up()
    if x or y != 0:
        t.goto(x, y)

    t.seth(tilt)
    

    #draw the moon - (with pen kept 'up' and does not show pen lines. Only fill colors)
    t.fillcolor(tail_color)
    t.begin_fill()
    t.forward(100 * scale)
    t.lt(158)
    t.forward(100 * scale)
    t.end_fill()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(width * scale)
    t.end_fill()

    
    
    #reset turtle
    t.seth(0)
#end - draw_comet
    

#-------------------------------------------------#
#-----------------atomic shapes-------------------#
#-------------------------------------------------#
def draw_tri(t, x, y, side1, fill, pen, tilt = 0, tri_type = 'equ_tri', side2 = None, angle = None):
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
    t.seth(tilt)
    t.down()
    t.fillcolor(fill)
    if pen is not None:
        t.pencolor(pen)

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


def draw_rec(t, x, y, side1, side2, fill, pen, tilt = 0):
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
    if pen is not None:
        t.pencolor(pen)
    #end - if pen
    if fill is not None:
        t.fillcolor(fill)
        t.begin_fill()
    #end - if fill
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


