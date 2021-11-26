'''
Project Name: Random Walk
Author:Jake McBride
Due Date: 11/DD/2021
Course: CS1400-602

Put your description here, lessons learned here,
and any other information someone using your
program would need to know to make it run.
'''

import sys
import random
import turtle

def main(): #main function is needed in all programs for automated testing
    '''
    
    '''
    #Initialize family member dictionaries 
    pa = {'name':'Pa', 'start':[0,0], 'cur_point':[0,0], 'ways':((1,0),(0,1),(-1,0),(0,-1))}
    ma = {'name':'Mi-Ma', 'start':[0,0], 'cur_point':[0,0], 'ways':((1,0),(0,1),(-1,0),(0,-1),(0,-1))}
    reg = {'name':'Reg', 'start':[0,0], 'cur_point':[0,0], 'ways':((1,0),(-1,0))}
    all = [pa, ma, reg]

    #Retrieve command line arguements
    try:
        steps = sys.argv[1]
        walks = sys.argv[2]
        who = sys.argv[3]
    except:
        steps = '100,1000'
        walks = '50'
        who = 'Pa'

    #Error checking for conversions
    try:
        #Convert 'steps' from string into a list of integers
        steps = steps.split(',')
        for i in range(len(steps)):
            steps[i] = int(steps[i])
        #Convert 'walks' from string into an integer
        walks = int(walks)
    except:
        return print('Please, ensure you enter "python3 <filename> <integer(steps)> <integer(walks)> <walker(s)>')
    # End - Error checking and conversions

    #Assign a dictionary with the corresponding name OR include all dictionaries
    if who == 'Pa':         who = pa
    elif who == 'Mi-Ma':    who = ma
    elif who == 'Reg':      who = reg 
    elif who == 'all':      who = all 
    else:
        return print('please enter "Pa", "Mi-Ma", "Reg", or "all" for the <walker>.')
    # End - dictionary assignmnet

# End - main()


def simulate(who, walks, steps):
    for i in who:
        do_walk(walks, steps)
# End - simulate()


def do_walk(walks, steps):
    for i in range(len(steps)):
        for k in range(walks):
            do_step(steps)
# End - do_walk()


def do_step(steps):
    for i in range(steps):
        # have the walker go in a random direction
        pass
    return        
# End - do_step()

def do_plot():
    plotter =  turtle.Turtle()
    # algorithm for plotting data points
# End - do_plot()



def get_mean():
    # calculate the mean of all of one walkers walks
    return
# End - get_mean()

def get_max():
    # calculate the max of all of one walkers walks
    return
# End - get_max()

def get_min():
    # calculate the min of all of one walkers walks
    return
# End - get_min()



if __name__ == '__main__':
    main()  #excucte main function
