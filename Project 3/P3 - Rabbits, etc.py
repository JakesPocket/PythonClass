"""
Project Name:Rabbits, Rabbits, Rabbits 
Author: Jake McBride
Due Date: 10/16/2021
Course: CS1400-602


Description:
This program will calculate how many months it will take 
to breed rabbits before running out of rabbit cages. And 
as the program runs it will calculate the amount of adult 
and baby rabbits for each month and write it to the output 
file.


New things I've learned:
    -open() - create an object to read or make and write to files
    -write() - add a line of data to a file
    -f strings - more formatting options for printing to screen 
    and files


ReadMe:
    No additional information needed.
"""


def do_research(cages, adults, babies):
    '''
    Calculates each month's amount of adult, baby, and total rabbits.
    Then writes this information to the rabbits.csv file
    Accepts parameters: cages, adults, and babies all need to be integers
    '''
    
    # init - variables
    month = 0
    total = 0

    #open access to rabbits.csv file and set access mode 'write'
    with open('rabbits.csv', 'w') as out:

        #add table heading
        out.write(f'# Table of rabbit pairs\n')
        out.write(f'Month, Adults, Babies, Total\n')

        #iterate blockcode until 'cages run out'
        while total < cages:
            
            #set new value for 'month' and 'total' variables
            month += 1
            total = adults + babies

            #write values of each variable for each month on a newline
            out.write(f'{month:5}, {adults:6}, {babies:6}, {total:5}\n')
            
            #usage of the fibonacci sequence using three variables
            new_babies = adults
            adults += babies
            babies = new_babies

        #end - while loop
        #write which month the cages ran out
        out.write(f'# Cages will run out in month {month}')

    #close rabbits.csv file
#end - do_research()

do_research(500, 1, 0)