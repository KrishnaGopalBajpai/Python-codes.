#A String is a sequence of characters.
#String can be created by enclosing characters inside a single quote or double quotes.
#Even triple quotes can be used in python but generally used to represent multiline string and docstrings.
#String are immutable.This means that elements of a string cannot be changed once it has declared.
#we can simple re-assign different strings with the same name. it support negative indexing.

#ex-1)
Name = "Krishna"
Para = """this is
my name """ 
paragr = "this is 
error code"
'''this will give us an error'''

Paragraph = '''this is a multiline 
string Paragraph. This is for testing. '''

print(Name)
print(Para)
print(Paragraph)

'''output:-
  File "main.py", line 4
    paragr = "this is 
                     ^
SyntaxError: EOL while scanning string literal
'''

#ex-2)
Name = "Krishna"
Para = """this is
my name """ 
Paragraph = '''this is a multiline 
string Paragraph. This is for testing. '''

print(Name)
print(Para)
print(Paragraph)

'''output:-
Krishna
this is
my name 
this is a multiline 
string Paragraph. This is for testing. 
'''
