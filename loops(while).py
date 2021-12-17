#The while loops in python is used to iterate over a block of code as long as the test expression(condition) is true.
#we generally use this loop when we don't know beforehand, the number of times to iterate.
# while test_expresion
#    body of while

#ex-1)
n = 5
while n>=0:
    print(n)
    n -=1

  '''
output:-
5
4
3
2
1
0
  '''
 #ex-2)
n = 5
while n>=0:
    print(n)
    
 '''
 output:- infinite loop.
 '''
#ex-3
n = 5
while n>=0:
    print(n, end=",")
    n -=1
'''
output:- 
5,4,3,2,1,0,
'''
