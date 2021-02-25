import os
import time

# open with read access
input_file = open('test.txt', 'r')
# open and overwrite
output_file = open('results.txt','w')

# read all the lines into a list of lines
line_list = input_file.readlines()
# walk the list of lines taking each line
for line in line_list:
    # find the local time
    time_now = time.asctime(time.localtime(time.time()))
    # write the time and the line to the file
    output_file.write(f'Time: {time_now} The message is: "{line.strip()}"\n')
    # The strip method can be used to strip off the \n from the end of the line
    # output_file.write(f'Time: {time_now} The message is: "{line.strip()}"\n')

# this is another way to do the same thing.
# read a single line from the file
line = input_file.readline()
while line: # if the line contains somethin
    print(line)
    # write the line to the output file
    output_file.write(line)
    # read another line and to back to the beginning of the loop
    line = input_file.readline()

