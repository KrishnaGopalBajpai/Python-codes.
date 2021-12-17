# if statement if test expression:
#                   statement(s)  

#ex1)

voter_age = 25
if voter_age >= 18:
    print('you can vote as your in the right age')

print('this will always be execute')

'''output:- you can vote as your in the right age
this will always be execute'''
#ex2)

voter_age = 3
if voter_age >= 18:
    print('you can vote as your in the right age')

print('this will always be execute')

'''output:- 
  this will always be execute '''


# if statement if test expression:
#                   body of if
#              else:
#                   body of else

#ex1)
voter_age = 25
if voter_age >= 18:
    print('you can vote as your is equal/greater to the voter_age')
else:
    print ('you can not vote as you are under the age of voter_age.')

print('this will always be execute')

'''
output:-
you can vote as your is equal/greater to the voter_age
this will always be execute
'''
#ex2)
voter_age = 13
if voter_age >= 18:
    print('you can vote as your is equal/greater to the voter_age')
else:
    print ('you can not vote as you are under the age of voter_age.')

print('this will always be execute')

''' output:- 
you can not vote as you are under the age of voter_age.
this will always be execute
'''

# if statement if test expression:
#                   body of if
#            elif test expression:
#                   body of elif
#                else:
#                   body of else

#ex1)pass a no to the verible and find the type interger of that.

num = 13
if num > 0:
    print('Positive number')
elif num == 0:
    print('zero')
else:
    print ('Negative number')
    
'''output:-
  Positive number
'''

#ex2)
num = 0
if num > 0:
    print('Positive number')
elif num == 0:
    print('zero')
else:
    print ('Negative number')
    
'''output:-
   zero
'''

#ex2)
num = -12
if num > 0:
    print('Positive number')
elif num == 0:
    print('zero')
else:
    print ('Negative number')

'''output:-
   Negative number
'''      
