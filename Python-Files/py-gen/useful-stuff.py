# useful file stuff
import os

# checks the path is there
os.path.exists('./here/afile.txt')
# finds the path to this file
here = os.path.abspath(__file__)
# finds the directory path not including the file
root = os.path.dirname(here)
# Creates string path to the jinja templates directory by joining two paths.
path_to_templates = os.path.join(root, 'jinja-templates')

# Opens the file for overwrite access
# 'r' for read, 'a' for append
ouptut_file = open('./mydir/myfile.txt', 'w')
# There wil be many methods available on output_file
# such as read, readline, write, writelin...
# Don't forget to close the file!


file_path = 'home/freddy/mydir/myfile.txt'
#  uses string split method to get a list
dir_list = file_path.split(sep='/')

import time
# secs since epoch
print(time.time())
#local time
print(time.localtime(time.time()))
# better
print(time.asctime(time.localtime(time.time())))

# String formatting
print('The {} is good.'.format('weather'))
print('The %s is good.'%('weather'))


missing_word = 'weather'
print('The {} is good.'.format(missing_word))

print('The %s is good.'%(missing_word))

print(f'The {missing_word} is good.')

