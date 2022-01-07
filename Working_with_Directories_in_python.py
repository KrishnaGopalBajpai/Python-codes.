#Get the current path:-

import os
print(os.getcwd())

#os.getcwd() → fetches the current directory

#Make a new directory:-

os.mkdir("new_dir")

#os.mkdir → makes a new directory

#Change Directory:-

os.chdir("new_dir")

#os.chdir → chnage directory

#Create a new file inside a directory

open('index.html', 'x')

#“x” is similar to “w”. But for “x”, if the file exists, raise FileExistsError.
#For “w”, it will simply create a new file / truncate the existed file.

#To go one step Back in the path hierarchy

os.chdir("../new_dir")

#chdir -> go one step back.

#List the contents of the directory

os.listdir("new_dir/website")

#listdir → method lists all the contents inside the directory

#Check whether content is a subdirectory or a file

for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")
        
 #os.path.join() method in Python join one or more path components intelligently.       

#Fetching the absolute path:-

def parent_directory():

  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.join(os.getcwd(), os.pardir)
  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())


#Moving Files and Directories

>>> import shutil
>>> shutil.move('Krishna/', 'code/')
'code'

#shutil.move('Krishna/', 'code/') moves Krishna/ into code/ if code/ exists. If code/ does not exist, Krishna/ will be renamed to code.

#Renaming Files and Directories  

os.rename('text.html', 'write.html')

#The line above will rename text.html to write.html. 
#If the destination path points to a directory, it will raise an OSError.
