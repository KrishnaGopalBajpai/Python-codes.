#To delete a file we first import the OS module. 
#The OS module in Python provides functions for interacting with the operating system. 
#OS comes under Python’s standard utility modules.

import os

delete_this_file = '<path of the file>'
os.remove(delete_this_file)
