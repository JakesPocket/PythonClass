'''
Project Name: Was Clinton Right?
Author: Jake McBride
Due Date: 12/17/2021
Course: CS1400-602

Description:
    This program will evaluate the data referenced in Clinton's statement from 2012 about private sector jobs.
    Then, based on the results of the evaluation, a conclusion of my own will be provided for the user to review
    in the "conclusion.md" file (and will also be available in the code file itself).

Things I've learned:
    - New algirithms using function calls
    - How to write better comments
    - f-string formatting (alignment & padding)
    - More about return value usage
    
ReadMe: My Full Conclusion... Spoiler!
	Bill Clinton's statement about the jobs produced during either party's years holding the White House
    was mostly accurate. Pulling the data from the government’s website and doing my own calculations show
    his  numbers regarding the years were spot on. Although his numbers of new jobs produced over those
    years were a bit off, jobs produced in years of the Democrats were still nearly doubled when compared to
    the Republicans. So, if the records of the government can be trusted, then Bill Clinton has some strong
    data supporting his statement! The facts check out close enough for me. When dealing in the tens of millions,
    a few million doesn't make much a difference.
                
    Bill Clintons’ Statement:
        “Since 1961, for 52 years now, the Republicans have held the White House 28 years, the Democrats 24.
        In those 52 years, our private economy has produced 66 million private-sector jobs. So what’s the
        jobs score? Republicans 24 million, Democrats 42 (million).”

    My calculations based on government records:
		   Republican Years: 28
		   Democratic Years: 24
		        Total Years: 52
		New Republican Jobs: 21,876,000
		New Democratic Jobs: 40,464,000
		     Total New Jobs: 62,340,000
    
    
'''
#-----------------------------------------------------main()------------------------------------------------------#
def main():
    '''
    # A - Initialize file variables by calling convert_file() and passing in the file names for each function call.
    # B - Calculate the new jobs per political party, total new jobs, and years per party who held the white house.
    # C - Write to file all the necessary results to support my conclusion.
    '''

    conclusion = '''
	Bill Clinton's statement about the jobs produced during either party's years holding the White House
    was mostly accurate. Pulling the data from the government’s website and doing my own calculations show
    his  numbers regarding the years were spot on. Although his numbers of new jobs produced over those
    years were a bit off, jobs produced in years of the Democrats were still nearly doubled when compared to
    the Republicans. So, if the records of the government can be trusted, then Bill Clinton has some strong
    data supporting his statement! The facts check out close enough for me. When dealing in the tens of millions,
    a few million doesn't make much a difference.
                
    Bill Clintons’ Statement:
        “Since 1961, for 52 years now, the Republicans have held the White House 28 years, the Democrats 24.
        In those 52 years, our private economy has produced 66 million private-sector jobs. So what’s the
        jobs score? Republicans 24 million, Democrats 42 (million).”

    My calculations based on government records:
                 '''
    
    # A
    job_data = convert_file(file_name='BLS_private.csv')
    presidents = convert_file(file_name='presidents.txt')
    
    # B
    total_new_jobs = total_new_jobs_per_party(job_data,presidents)
    
    # C
    
    with open('conclusions.md', 'w') as conclusion_file:
        print(f'\t{conclusion.strip()}', file = conclusion_file)
        for key in total_new_jobs:
            print (f'\t\t{key:>19}: {total_new_jobs[key]:,}', file=conclusion_file) #print (write) to file

# End - main()


#-------------------------------------------------convert_file()--------------------------------------------------#
def convert_file(file_name):
    ''' Parameters - file_name = type: string

    Open file and iterate the lines it into a dictionary:
        Assign the current lines year (first element) to a new 'key' in the dictionary.
        Assign the rest of the current line as a list (elements = values in between commas) to the value paired with current key
    Return the dictionary.
    '''

    current_dict = {} # Initialize dictionary
    with open(file_name, 'r') as current_file:
        for line in current_file:
            new_list = line.strip().split(',')
            current_dict[new_list[0]] = new_list[1:]
        # End - for loop
    # End - with open()

    return current_dict

#End - convert_file()

#-------------------------------------------total_new_jobs_per_party()--------------------------------------------#
def total_new_jobs_per_party(jobs,presidents):
    ''' Parameters - jobs = type: dict, presidents = type: dict

    Iterate through the keys and subtract the first element from the last in each list in the dictionary:
        Add to either party variable the difference between the first and last elements (this being the new jobs 'produced' for that year)
    Return a new dictionary with the labeled results as key-value pairs (multiply each by 1,000 since the 'private jobs' document states this)
    '''
    # Initialize variables
    new_rep_jobs, new_dem_jobs = 0, 0
    rep_years, dem_years = 0, 0
    for year in jobs: # Iterate through the dictionary keys, each key is a year as type string. example: '1961'
        if presidents[year][1] == 'Republican':
            rep_years += 1
            new_rep_jobs += int(jobs[year][-1]) - int(jobs[year][0])
        elif presidents[year][1] == 'Democrat':
            dem_years += 1
            new_dem_jobs += int(jobs[year][-1]) - int(jobs[year][0])
        # End - if statement
    # End - for loop
    
    # Return a dictionary of labeled totals     
    return {'Republican Years': rep_years,
            'Democratic Years':dem_years,
            'Total Years':rep_years + dem_years,
            'New Republican Jobs':new_rep_jobs * 1000,
            'New Democratic Jobs':new_dem_jobs * 1000,
            'Total New Jobs':(new_rep_jobs + new_dem_jobs) * 1000}

# End - total_new_jobs_per_party()


# Only True if this file is ran directly
if __name__ == '__main__':
    main()  # Execute main function


