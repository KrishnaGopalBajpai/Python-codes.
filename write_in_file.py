#By default the mode of the open keyword is ‘read’ only. To write we need to use ‘write’ mode.
#Caution : It will delete the old content in the file and replaces it with the new content specified.

with open("my_file.txt", mode ="w") as file:
    file.write("New Text.")
