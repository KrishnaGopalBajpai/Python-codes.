#python for loops
#The for in python is used to iterate over a sequence(list, tuple, string) or others iterable objects.
#Iterating over a sequence is called traversal.
'''for val in sequence
    body of for '''

#ex-1) Table of 2.
for  x in range(1,11):
    print(2*x)
''' 
output:-
2
4
6
8
10
12
14
16
18
20
'''

#ex-1) numbers with difference of 2.
for  x in range(10):
    print(2*x)
''' 
output:-
0
2
4
6
8
10
12
14
16
18
'''
#ex-3)
for  x in range(10):
    print(2*x, end=",")

''' 
output:-
0,2,4,6,8,10,12,14,16,18,
'''
#ex-4)
for  x in range(10):
    print(2*x, end=",")
a = ['Anuj', 'Rohit','Shivam']
for name in a:
    print(2*name, end=" ,")
''' 
output:-
0,2,4,6,8,10,12,14,16,18,AnujAnuj ,RohitRohit ,ShivamShivam ,
'''
#ex-5)
a = ['Anuj', 'Rohit','Shivam']
for name in a:
    print(name*4, end=" ,")
''' 
output:-
AnujAnujAnujAnuj ,RohitRohitRohitRohit ,ShivamShivamShivamShivam ,
'''
