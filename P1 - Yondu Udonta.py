'''
Project Name: Yondu Udonta
Author: Jake McBride
Due Date: 
Course: CS1400-zzz

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
'''

def main():
    '''
    Program starts here.
    '''
    reavers = input("How many Reavers: ")
    reavers = int(reavers)
    
    units = input("How many units: ")
    units = int(units)
    
    if reavers < 1 or units < 1:
        print("Error: Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Error: Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return
    
    '''
    Students, put your code here.   
    '''

   
#end of main()

if __name__ == "__main__":
    main()
    