# python program to implement full adder
 
# Function to print sum and C-Out
def fulladder(A, B, C):
 
    # Calculating value of sum
    Sum = A ^ B ^ C
    
    # Calculating value of C-Out
    C_Out = (A & B)|(C & (A ^ B))
 
    # printing the values
    print("Sum = ", Sum)
    print("C-Out = ", C_Out)
 
 
# Driver code
A = int(input ("Enter the value A:"))
B = int(input ("Enter the value B:"))
C = int(input ("Enter the value C:"))
# passing three inputs of fulladder as arguments to get result function
fulladder(A, B, C)
  
  
  
#log Vaule from all 8 cases generated in a full adder. 
  1)Enter the value A:0
    Enter the value B:0
    Enter the value C:0 
    Sum =  0
    C-Out =  0
  2)Enter the value A:0 
    Enter the value B:0
    Enter the value C:1
    Sum =  1
    C-Out =  0
  3)Enter the value A:0
    Enter the value B:1
    Enter the value C:0
    Sum =  1
    C-Out =  0
  4)Enter the value A:0
    Enter the value B:1
    Enter the value C:1
    Sum =  0
    C-Out =  1
  5)Enter the value A:1  
    Enter the value B:0
    Enter the value C:0
    Sum =  1
    C-Out =  0
  6)Enter the value A:1
    Enter the value B:0
    Enter the value C:1
    Sum =  0
    C-Out =  1
  7)Enter the value A:1
    Enter the value B:1
    Enter the value C:0
    Sum =  0
    C-Out =  1
  8)Enter the value A:1
    Enter the value B:1
    Enter the value C:1
    Sum =  1
    C-Out =  1
  
