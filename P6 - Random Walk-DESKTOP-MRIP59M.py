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

def main():
    '''
    
    '''

    #Retrieve command line arguements
    try:
        walk_lengths = list(map(int,sys.argv[1].split(','))) #Convert 'steps' from string into a list of integers
        walks = int(sys.argv[2]) #Convert 'walks' from string into an integer
        walker = sys.argv[3]
    except:
        walk_lengths = [100,1000]
        walks = 50
        walker = 'all'

        print('Please, ensure you enter "python3 <filename> <integer(steps)> <integer(walks)> <walkers(s)>')
        #return
        
    # End - Error checking and conversions
    walkers = get_data_structures(walker)


    simulate(walkers, walks, walk_lengths)


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
    if walker == 'Pa':         walkers = [pa]
    elif walker == 'Mi-Ma':    walkers = [ma]
    elif walker == 'Reg':      walkers = [reg] 
    elif walker == 'all':      walkers = [pa, ma, reg]
    else: return print('please enter "Pa", "Mi-Ma", "Reg", or "all" for the <walkers> parameter.')
    # End - dictionary assignmnet
    return walkers

def simulate(walkers, walks, walk_lengths):
    '''
    
    '''
    for who in walkers:
        for steps in walk_lengths:
            do_walk_trials(who, walks, steps)
            plot() if steps == 100 else None # Plot data points for the current 'walker' in walk of 100 steps
            calc_and_print_mmmcv(who, steps)
# End - simulate()

def do_walk_trials(who, walks, steps):
    '''
    
    '''
    for _ in range(walks):
        who['now_point'] = who['start'] # Reset starting point

        take_a_walk(who, steps)

        who['end_points'] += [take_a_walk(who, steps)]

        
# End - do_walk_trials()

def take_a_walk(who, steps):
    '''
    
    '''
    for _ in range(steps): 
        who['now_point'] = [x + y for x, y in zip(who['now_point'], random.choice(who['ways']) )]
    return who['now_point']
    
# End - take_a_walk()





def plot():
    plotter =  turtle.Turtle()
    plotter.hideturtle()
    plotter.up()
    plotter.seth(90)
    plotter.speed(0)

    walks = 50
    steps = 100
    
    walkers = get_data_structures('all')
    for who in walkers:
        do_walk_trials(who, walks, steps)
        calc_and_print_mmmcv(who, steps)
        if who['name'] == 'Pa':     plotter.shape('circle'); plotter.color('black')
        if who['name'] == 'Mi-Ma':  plotter.shape('square'); plotter.color('green')
        if who['name'] == 'Reg':    plotter.shape('triangle'); plotter.color('red')

        for x, y in who['end_points']: plotter.goto(x, y); plotter.stamp()



    save_to_image()

# End - do_plot()




def calc_and_print_mmmcv(who, steps):
    '''
    calculate the Mean, Max, Min, and CV of all of one walkerss walks
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
# End - get_mean_max_min()





if __name__ == '__main__':
    main()  #excucte main function


