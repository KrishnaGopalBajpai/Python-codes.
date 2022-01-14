# Function to print sum and C-Out
def Fullsubtractor (A, B, C):
 
    # Calculating value of sum
    Difference = A ^ B ^ C
    
    # Calculating value of C-Out (A-B-C)
    Borrow = (~A & B)|(B & C)|(~A & C)
    
    #Second type of carry out equation (B-A-C)
    #Borrow = (A & ~B)|(~B & C)|(A & C)
 
    # printing the values
    print("Difference = ", Difference)
    print("Borrow = ", Borrow)
 
 
# Driver code
A = int(input ("Enter the value A:"))
B = int(input ("Enter the value B:"))
C = int(input ("Enter the value C:"))

# passing three inputs of fulladder as arguments to get result function
Fullsubtractor (A, B, C)


#log output:- 

#log Vaule from all 8 cases generated in a full adder. 
  1)Enter the value A:0
    Enter the value B:0
    Enter the value C:0 
    Difference =  0
    Borrow =  0
  2)Enter the value A:0 
    Enter the value B:0
    Enter the value C:1
    Difference =  1
    Borrow =  1
  3)Enter the value A:0
    Enter the value B:1
    Enter the value C:0
    Difference =  1
    Borrow =  1
  4)Enter the value A:0
    Enter the value B:1
    Enter the value C:1
    Difference =  0
    Borrow =  1
  5)Enter the value A:1  
    Enter the value B:0
    Enter the value C:0
    Difference =  1
    Borrow =  0
  6)Enter the value A:1
    Enter the value B:0
    Enter the value C:1
    Difference =  0
    Borrow =  0
  7)Enter the value A:1
    Enter the value B:1
    Enter the value C:0
    Difference =  0
    Borrow =  0
  8)Enter the value A:1
    Enter the value B:1
    Enter the value C:1
    Difference =  1
    Borrow =  1
