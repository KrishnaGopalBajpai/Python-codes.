#Python lists:-
#note:- python is the type agnostic languange. and lists are mutable in nature.
#In python programming a list is created by placing all the items(elements) inside a square bracket[],
#separated by commas.
#it can have any number of items and they may be of different types (integer, float, string etc.)
#1. my_list = []
#2. my_list = [ 1, 2, 3]
#3. my_list = [1, 'Hello', 3.4]

#Ex=1)
my_list = [1,2,3]
print(my_list)

name = 'anuj'
name = 123
name = [1,2,3,'anuj']
print(name)
fruits = ["Apple",'Guava', 'Papaya']
print(fruits[2])
print(fruits[-1])

num =[1,2,3,4,5]
print(num[2:5])
print(num[0:5:2])
print (num[::-1])
print(num[-1:0:-2])
num[3] = 'krishna'
print(num)

del num[3]
print(num)

'''output:-
[1, 2, 3]
[1, 2, 3, 'anuj']
Papaya
Papaya
[3, 4, 5]
[1, 3, 5]
[5, 4, 3, 2, 1]
[5, 3]
[1, 2, 3, 'krishna', 5]
[1, 2, 3, 5]'''



