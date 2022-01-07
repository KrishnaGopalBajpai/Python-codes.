#for appending to a file #we change the mode to “a” instead of “w”. The old content in the file remains 
#intact while the new content specified gets appended or added onto the file alongwith the old content.


with open("my_file.txt", mode ="a") as file:
    file.write("\nAppended content")
    
