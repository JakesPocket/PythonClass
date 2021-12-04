'''
Project Name: Random Walk
Author:Jake McBride
Due Date: 11/DD/2021
Course: CS1400-602

Description:

New things I've learned:
    -New algirithms
    -List compr


ReadMe:

'''
import sys
import random       # to randomly select which 'direction' to go: using random.choice(who['ways'])
import turtle       # to display the data points in a graphic window
import statistics   # to find the 'mean' and 'standard deviation' of data in the 'distances' list
import subprocess   # to save the turtle plot as an image

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main(): # main() will only be called if this file (random_walk.py) is ran directly
    ''' 
    If ran directly...
    This function will retrieve 3 command line arguements
    Then will call simulate() using those arguements
    '''
    #Retrieve command line arguements
    try:
        trials = list(map(int,sys.argv[1].split(','))) #Convert 'steps' from string into a list of integers
        walks_per_trial = int(sys.argv[2]) #Convert 'walks' from string into an integer
        walkers = sys.argv[3]
    # If any arguement is bad or missing  --- return Error
    except:
        print('Error: Ensure you enter "python3 <filename> <integer(steps)> <integer(walks)> <walker>"')
        return
    simulate(trials, walks_per_trial, walkers)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def simulate(trials, walks_per_trial, walkers):
    ''' calls functions '''

    walkers = initialize(walkers)
    do_trials(walkers, walks_per_trial, trials)
    plot()
# End - simulate()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def do_trials(walkers, walks_per_trial, trials):
    ''' Calls do_walk_trials() passing through three arguments '''
    #with open('hello', 'a') as foo:
        #foo.writelines(f'{walkers, walks_per_trial, trials}')
    for who in walkers:
        for steps_per_walk in trials:
            for _ in range(walks_per_trial):
                who['now_point'] = who['start']
                for __ in range(steps_per_walk):
                    who['now_point'] = [x + y for x, y in zip(who['now_point'], random.choice(who['ways']) )]
                # End - for _ in steps_...
                who['end_points'] += [who['now_point']]
            # End - for _ in walks_...
    # End for...

    get_mean_max_min__cv(walkers, trials)

# End - do_trials()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def initialize(walkers):
    ''' intitializes walkers and data '''
    # Assign starting point and directions to variables
    start_point = [0,0]
    north, east, south, west = [0, 1],[1, 0],[0, -1],[-1, 0]

    # Assign walker dictionaries
    #----------------------Pa-----------------------#
    _pa = { 'name':'Pa',
            'start':start_point,
            'now_point':[0,0],
            'ways':(north, east ,south ,west),
            'end_points':[]}
    #---------------------Mi-Ma----------------------#
    _ma = { 'name':'Mi-Ma',
            'start':start_point,
            'now_point':[0,0],
            'ways':(north, east ,south ,south ,west),
            'end_points':[]}
    #----------------------Reg-----------------------#
    reg = { 'name':'Reg', 
            'start':start_point,
            'now_point':[0,0],
            'ways':(east, west),
            'end_points':[]}

    #Assign a dictionary with the corresponding name OR include all dictionaries
    if walkers == 'Pa':         return [_pa]
    elif walkers == 'Mi-Ma':    return [_ma]
    elif walkers == 'Reg':      return [reg]
    elif walkers == 'all':      return [_pa, _ma, reg]
    else:                       return print('please enter "Pa", "Mi-Ma", "Reg", or "all" for the <walkers> parameter.')
# End - initialize(walkers)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_mean_max_min__cv(walkers, trials):
    '''
    Calculate the Mean, Max, Min, and _cv of all of one walkerss walks_per_trial
    Parameters:
    who - the current walker/dictionary
    steps_per_walk - number of steps taken from trials
    '''
    # Initialize a list
    distances = [1,2]
    for who in walkers:
        for steps_per_walk in trials:
            # List Comprehension - Fill list by iterating the 'endpoints' list and calculating the distances with Pythagoras theorem
            distances = [a ** 2 + b ** 2 for a, b in who['end_points']]

            min_d = min(distances) ** (1/2)
            max_d = max(distances) ** (1/2)
            avg_d = statistics.mean(distances) ** (1/2)
            std_dev = statistics.stdev(distances) ** (1/2)
            _cv = std_dev / avg_d

            print(f"{who['name']} random walk of {steps_per_walk} steps")
            print(f"Mean = {avg_d:.1f} CV = {_cv:.1f}")
            print(f"Max = {max_d:.1f} Min = {min_d:.1f}")
        # End - for steps_...
    # End - for who...
# End - get_mean_max_min__cv()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def plot():
    ''' Does the thing '''
    pete =  turtle.Turtle() # Pete is a turtle
    pete.hideturtle()       # Pete is a stealthy turtle
    pete.up()               # Pete's tail is always up and wagging
    pete.speed(0)
#     turtle.tracer(0,0)      # Prevents drawing until complete and displays all points at once
    
    walkers = initialize('all')
    for who in walkers:

        if who['name'] == 'Pa':     pete.shape('circle'); pete.color('black')
        if who['name'] == 'Mi-Ma':  pete.shape('square'); pete.color('green')
        if who['name'] == 'Reg':    pete.shape('triangle'); pete.color('red')

        for x, y in who['end_points']: pete.goto(x, y); pete.stamp()
    # End - for who...
    save_to_image()

def save_to_image():
    '''Saves the turtle canvas to 'random_walk.png'. Do not modify this function.
    '''
    turtle.getcanvas().postscript(file='random_walk.eps')
    subprocess.run(['gs',
                    '-dSAFER',
                    '-o',
                    'random_walk.png',
                    '-r200',
                    '-dEPSCrop',
                    '-sDEVICE=png16m',
                    'random_walk.eps'],
                   stdout=subprocess.DEVNULL)



if __name__ == '__main__':
    main()  #excucte main function

