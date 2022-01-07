#Method1:-
 
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

#The second method in which we have used with open(…) as "…" Pattern. The ‘with’ keyword is used when working with unmanaged resources such as file streams.
#In method 1 we are explicitly closing the file after reading it. However, the ‘with’ keyword itself takes care of the ‘exit()’ method.
#note:- To save Processing time we use 'with'.

#Method2:-

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
