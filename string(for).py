#for loops with string.
#   for letter in 'Hello':
#         print(letter*2, end=",")

#ex-1)
for letter in 'Krishna':
    print(letter*2, end=",")
'''
output:-
KK,rr,ii,ss,hh,nn,aa,
'''

#ex-2)
a ="abc"
b ="def"
c =a+b
print(c)

'''output:-
abcdef
'''
#ex-3)
a ="abc"
for my_char in a:
    print(my_char*2)
'''output:-
aa
bb
cc
'''
#Ex-4)
a ="abc"
for my_char in a:
    print(my_char*2)
    print(my_char*2,end=",")

'''output:-
aa
aa,bb
bb,cc
cc
'''
