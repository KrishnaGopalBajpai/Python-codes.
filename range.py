#we can generate a sequence of numbers using range() function on the go not stored them in.
#suppose range(10) will generate number from 0 to 9 (10 nos). -> [0,1,2,3,4,5,6,7,8,9]
#syntex : range ((inclusive)start,(exclusive)stop,stepsize). defaults value of stepsize is one if not given.

#ex1)

a = range (10)

print (a)

'''
output:- range(0, 10)
'''
#ex2) list the number from 0 to 9.
a = list (range (10))

print (a)

'''
output:- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''


#ex3) list the number from 5 to 9.
a = list (range (5,10))

print (a)

'''
output:- [5, 6, 7, 8, 9]
'''

#ex2) list the number from 0 to 10 with stepsize2.
a = list (range (0,11,2))

print (a)

'''
output:- [0, 2, 4, 6, 8, 10]
'''
