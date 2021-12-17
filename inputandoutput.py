#inputandoutput.
#input() used for the user define input.
#print()

name = input()
print (type (name))
print (name)
print ('you entered', name)

''' output:- 
mona (given input to console)
<class 'str'>
mona
you entered mona
'''

#ex-1) make a multiplier of two nos. 
a = input ()
b = input ()
print (type(a))
print (type(b))
c=a*b
print(c)

'''output:-
4
5
<class 'str'>
<class 'str'>
Traceback (most recent call last):
  File "main.py", line 7, in <module>
    c=a*b
TypeError: can't multiply sequence by non-int of type 'str'
'''
#ex-2) make a multiplier of two nos. 
a = int (input ())
b = int (input ())
print (type(a))
print (type(b))
c=a*b
print(c)

'''
output :- 
4
5
<class 'int'>
<class 'int'>
20
'''

#ex-3) make a multiplier of two nos. 
a = int (input ('enter a'))
b = int (input ('enter b'))
print (type(a))
print (type(b))
c=a*b
print(c)

'''
output:- 
enter a300
enter b400 
<class 'int'>
<class 'int'>
120000
'''

#ex-4) write a program to take marks of a user 
#in english, science and Maths and print 
#the average of of these marks.

english_marks = int (input ('english_marks'))
science_marks = int (input ('science_marks'))
maths_marks = int (input ('maths_marks'))
print (type(english_marks))
print (type(science_marks))
print (type(maths_marks))
average = (english_marks+science_marks+maths_marks)/3
print('average_marks',average)

'''output:-
english_marks90
science_marks87
maths_marks74
<class 'int'>
<class 'int'>
<class 'int'>
average_marks 83.66666666666667
'''
