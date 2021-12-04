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

import sys          # to retrieve command-line input
import random       # to randomly select which 'direction' to go: using random.choice(who['ways'])
import turtle       # to display the data points in a graphic window
import statistics   # to find the 'mean' and 'standard deviation' of data in the 'distances' list
import subprocess   # to save the turtle plot as an image

def simulate(walkers, walks, walk_lengths):
    '''
    
    '''

    #Retrieve command line arguements
    '''
    try:
        walk_lengths = list(map(int,sys.argv[1].split(','))) #Convert 'steps' from string into a list of integers
        walks = int(sys.argv[2]) #Convert 'walks' from string into an integer
        walker = sys.argv[3]
    except:
        walks = 50
        walk_lengths = [100,1000]
        walker = 'all'
        print('Please, ensure you enter "python3 <filename> <integer(steps)> <integer(walks)> <walkers(s)>')
        return
    '''
    random.seed(9387482)
    walkers = get_data_structures(walkers)
    do_trials(walkers, walks, walk_lengths)
    plot()

# End - main()

def get_data_structures(walker):

    # Assign starting point and directions to variables
    start_point = [0,0]
    N, E ,S ,W = [0, 1],[1, 0],[0, -1],[-1, 0]
    
    # Initialize family member dictionaries 
    pa = { 'name':'Pa', 'start':start_point, 'now_point':[0,0], 'ways':(N, E ,S ,W), 'end_points':[], 'longest':0, 'shortest':0, 'average':0}
    ma = { 'name':'Mi-Ma', 'start':start_point, 'now_point':[0,0], 'ways':(N, E ,S ,S ,W), 'end_points':[], 'longest':0, 'shortest':0, 'average':0}
    reg = { 'name':'Reg', 'start':start_point, 'now_point':[0,0], 'ways':(E, W), 'end_points':[], 'longest':0, 'shortest':0, 'average':0}

    #Assign a dictionary with the corresponding name OR include all dictionaries
    if walker == 'Pa':         return [pa]
    elif walker == 'Mi-Ma':    return [ma]
    elif walker == 'Reg':      return [reg] 
    elif walker == 'all':      return [pa, ma, reg]
    else: return print('please enter "Pa", "Mi-Ma", "Reg", or "all" for the <walkers> parameter.')
    # End - dictionary assignmnet



def do_walk_trials(walkers, walks, walk_lengths):
    ''' Calls do_walk_trials() passing through three arguments '''
    for who in walkers:
        with open('hello.txt', 'a') as foo:
            foo.writelines(f'{walkers}\n')
        for steps in walk_lengths:
            for _ in range(walks):
                who['now_point'] = who['start']
                for _ in range(steps): 
                    who['now_point'] = [x + y for x, y in zip(who['now_point'], random.choice(who['ways']) )]
                    
                who['end_points'] += who['now_point']
    get_mean_max_min_cv(who, 100)

# End - simulate()









def get_mean_max_min_cv(who, steps):
    '''
    Calculate the Mean, Max, Min, and CV of all of one walkerss walks
    Parameters:
    who - the current walker/dictionary
    steps - number of steps taken from walk_lengths
    '''
    # Initialize a list
    distances = [] 
    # List Comprehension - Fill list by iterating the 'endpoints' list and calculating the distances with Pythagoras theorem
    distances = [a ** 2 + b ** 2 for a, b in who['end_points']]

    min_d = min(distances) ** (1/2) / 5
    max_d = max(distances) ** (1/2) / 5
    avg_d = statistics.mean(distances) ** (1/2) / 5
    std_dev = statistics.stdev(distances) ** (1/2) / 5
    cv = std_dev / avg_d
#     print(distances)
    print(f"{who['name']} random walk of {steps} steps")
    print(f"Mean = {avg_d:.1f} CV = {cv:.1f}")
    print(f"Max = {max_d:.1f} Min = {min_d:.1f}")
# End - get_mean_max_min_cv()


def plot():
    pete =  turtle.Turtle() # Pete is a turtle
    pete.hideturtle()       # Pete is a stealthy turtle
    pete.up()               # Pete's tail is always up and wagging
    pete.speed(0)           # Pete is a very fast turtle
    
    walks = 50
    steps = [100]
    walkers = get_data_structures('all')
    for who in walkers:
        simulate(who, walks, steps)

        if who['name'] == 'Pa':     pete.shape('circle'); pete.color('black')
        if who['name'] == 'Mi-Ma':  pete.shape('square'); pete.color('green')
        if who['name'] == 'Reg':    pete.shape('triangle'); pete.color('red')

        for x, y in who['end_points']: pete.goto(x, y); pete.stamp()
    save_to_image()


# End - do_plot() Thanks for your help, Pete!

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



