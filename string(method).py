#Mehods:- isalpha(), isdigit(), islower(), isupper(), lower(), upper() , lstrip(), rstrip().

#ex-1)

password = "abcdABA"
print(password.isalpha())

password = "abcdABA12&"
print(password.isalpha())

s = "12345"
print(s.isdigit())
s= "12345$ab"
print(s.isdigit())

p= "abcds"
m= "1223456"
n= "klnnsalmABCD"
print('p.isalpha', p.isalpha())
print('m.isdigit', m.isdigit())
print('n.islower', n.islower())
print('n.isupper', n.isupper())

print('n.lower', n.lower())
print('n.upper', n.upper())

'''Output:-
True
False
True
False
p.isalpha True
m.isdigit True
n.islower False
n.isupper False
n.lower klnnsalmabcd
n.upper KLNNSALMABCD '''

#ex-2)
password = "abcdABA"
print(password.isalpha())

password = "abcdABA12&"
print(password.isalpha())

s = "12345"
print(s.isdigit())
s= "12345$ab"
print(s.isdigit())

p= "abcds"
m= "1223456"
n= "klnnsalmABCD"
print('p.isalpha', p.isalpha())
print('m.isdigit', m.isdigit())
print('n.islower', n.islower())
print('n.isupper', n.isupper())

print('n.lower', n.lower())
print('n.upper', n.upper())

x= '   abc   '
print(x.lstrip())
print(x.rstrip())
print(x.upper())
print(x.lower())

my_ver = x.upper()
print(my_ver)
my_ver = x.lower()
print(my_ver)

''' Output:-
True
False
True
False
p.isalpha True
m.isdigit True
n.islower False
n.isupper False
n.lower klnnsalmabcd
n.upper KLNNSALMABCD
abc   
   abc
   ABC   
   abc   
   ABC   
   abc   
'''
