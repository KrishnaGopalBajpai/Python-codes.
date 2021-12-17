#he Break statement terminates the loop containing it.
#The continue statement is used to skip the rest of the code inside a loop for the current iteration only
#loop doesn't terminates but continues on with the next iteration.

#Ex-1) loop terminate after the print of 6.

for i in range (10):
    if i>6:
        break
    print(i)
    
'''
output:- 
0
1
2
3
4
5
6
'''

#ex-2)
for i in range (10):
    if i>6:
        break
    print(i, end = ",")

'''
output:- 
0,1,2,3,4,5,6,
'''

#ex-2) to escape the current iteraion.

for i in range (10):
    if i==8:
        continue
    print(i, end = ",")
    
'''output:-
0,1,2,3,4,5,6,7,9,
'''
  
