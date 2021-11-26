"""
Project Name:Library of Congress
Author:Jake MCbride
Due Date: 10/30/2021
Course: CS1400-602

Put your description here, lessons learned here,
and any other information someone using your
program would need to know to make it run.
"""



import sys

def main():

    if len(sys.argv) != 2:
        print('Error! Expected usage is C:\\dir_path>python program_name.py file_name.txt')
        return
    else:
        read_file = sys.argv[1]

    #creates a dictionary that will organize all lines by book title (key)
    sources = {}

    #open file and catch FileNotFoundError
    try:
        with open(read_file, 'r', encoding = 'utf-8') as in_file:
            file_lines = in_file.readlines()
    except FileNotFoundError:
        print(f'File {read_file} not found.')
        return

    for line in file_lines:
        new_line = line.strip().split('|')
        new_line.append(len(new_line[0]))
        new_line[1] = int(new_line[1])

        if new_line[2] in sources:
            sources[new_line[2]].append(new_line)
        else:
            sources[new_line[2]] = [new_line]
        #end - if new_line
    #end - for line

    #creates a list of the dictionary "sources" keys and sorts them
    sorted_sources = list(sources.keys())
    sorted_sources.sort()

    for book in sorted_sources:
        #sort sources[book] in order to obtain longest and shortest lines
        sources[book].sort(key = lambda x:x[3])

        #get longest line and shortest line
        longest = sources[book][-1]
        shortest = sources[book][0]
        actual_longest = []
        actual_shortest = []


        #get sum of all line text lengths and calculate average
        average = 0
        #sort by line number and write to file
        sources[book].sort(key = lambda x:x[1])

        with open('novel_text.txt', 'a') as text:
            text.writelines(f'{book}\n')

        for i in sources[book]:
            with open('novel_text.txt', 'a') as text:
                text.writelines(f'{i[0]}\n')
            average += i[3]
            if i[3] == shortest[3]:
                actual_shortest.append(i)
            if i[3] == longest[3]:
                actual_longest.append(i)
        #end - for i
        shortest = actual_shortest[0]
        longest = actual_longest[-1]

        with open('novel_text.txt', 'a') as text:
            if book != sorted_sources[2]:
                text.writelines('-----\n')
        average = round(average / len(sources[book]))

        with open('novel_summary.txt', 'a') as summary:
            summary.writelines(f'\n{book}\nLongest line ({longest[1]}): {longest[0]}\nShortest line ({shortest[1]}): {shortest[0]}\nAverage length: {average}\n')

if __name__ == "__main__":
    main()
    