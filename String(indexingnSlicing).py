#String Support negative indexing in python.
#Sclicing:- is the sub string of the string.
#Accessing Characters in a string(slicing)
#We can access individual characters using indexing and range of characters using sclicing.Index Starts from 0.
#Trying to access a character out of index range will raise an indexerror. The index must be an integer.
#Python allows negative indexing for its sequences.
#The index of -1 refers to the last item, -2 to the second last and so no.We can access a range in a string by 
#by using sclicing operator (cloning).

#ex-1)
fruit = "Apple"
print(fruit[0])
print(fruit[3])
print(fruit[5])

''' Output:-
A
l
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print(fruit[5])
IndexError: string index out of range
'''

#ex-2)
ruit = "Apple"
print(fruit[0])
print(fruit[3])
print(fruit[4])
print(fruit[-5])
print(fruit[-1])

'''output:-
A
l
e
A
e
'''
#ex-3) Sclicing 
fruit = "Apple"
print(fruit[0])
print(fruit[3])
print(fruit[4])
print(fruit[-5])
print(fruit[-1])

my_char = fruit[3];
print(my_char)
my_chara = fruit[4];
print(my_chara)

'''output:-
A
l
e
A
e
l
e
'''
#ex-4)
fruit = "Apple"
print(fruit[0])
print(fruit[3])
print(fruit[4])
print(fruit[-5])
print(fruit[-1])

my_char = fruit[3];
print(my_char)
my_chara = fruit[4];
print(my_chara)
my_sclice = fruit[0:5]
print(my_sclice)
my_sclic = fruit [3:5]
print(my_sclic)
my_scli = fruit [-5:-1]
print(my_scli)

'''output:- 
A
l
e
A
e
l
e
Apple
le
Appl'''

#ex-5)
fruit = "Apple"
print(fruit[0])
print(fruit[3])
print(fruit[4])
print(fruit[-5])
print(fruit[-1])

my_char = fruit[3];
print(my_char)
my_chara = fruit[4];
print(my_chara)
my_sclice = fruit[0:5]
print(my_sclice)
my_sclic = fruit [3:5]
print(my_sclic)
my_scli = fruit [-5:-1]
print(my_scli)
my_scl = fruit[:5]
print(my_scl)
my_sc = fruit[3:]
print(my_sc)
my_s = fruit[0:5:2] '''print the char by step 2'''
print(my_s)

'''Output:- 
A
l
e
A
e
l
e
Apple
le
Appl
Apple
le
Ape
'''

#ex-1)
fruit = "Apple"
print(fruit[0])
print(fruit[3])
print(fruit[4])
print(fruit[-5])
print(fruit[-1])

my_char = fruit[3];
print(my_char)
my_chara = fruit[4];
print(my_chara)
my_sclice = fruit[0:5]
print(my_sclice)
my_sclic = fruit [3:5]
print(my_sclic)
my_scli = fruit [-5:-1]
print(my_scli)
my_scl = fruit[:5]
print(my_scl)
my_sc = fruit[3:]
print(my_sc)
my_s = fruit[0:5:2]
print
'''reversed String by negative sclicing'''

my_re_sclice = fruit[::-1]
print(my_re_sclice)
my_re_sclic = fruit[::-2]
print(my_re_sclic)

''' output:- 
A
l
e
A
e
l
e
Apple
le
Appl
Apple
le
elppA
epA'''

#ex- 
fruit = "Apple"
print(fruit[0])
print(fruit[3])
print(fruit[4])
print(fruit[-5])
print(fruit[-1])

my_char = fruit[3];
print(my_char)
my_chara = fruit[4];
print(my_chara)
my_sclice = fruit[0:5]
print(my_sclice)
my_sclic = fruit [3:5]
print(my_sclic)
my_scli = fruit [-5:-1]
print(my_scli)
my_scl = fruit[:5]
print(my_scl)
my_sc = fruit[3:]
print(my_sc)
my_s = fruit[0:5:2]
print
'''reversed String by negative sclicing'''

my_re_sclice = fruit[::-1]
print(my_re_sclice)
my_re_sclic = fruit[::-2]
print(my_re_sclic)
my_re_scli = fruit[0:5:-1]
print(my_re_scli)
my_re_scl = fruit[-1:0:-1] '''Step should we define with the direction(+/-).'''
print(my_re_scl)
my_re_sc = fruit[-1:-6:-1]
print(my_re_sc)
my_re_s = fruit[-1:-6:1]
print(my_re_s)

'''output:- 
A
l
e
A
e
l
e
Apple
le
Appl
Apple
le
elppA
epA

elpp
elppA
''
'''
