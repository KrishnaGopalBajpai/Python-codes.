# Function to print sum and C-Out
def Halfsubtractor (A, B):
 
    # Calculating value of sum
    Difference = A ^ B 
    
    # Calculating value of C-Out (A-B)
    Borrow = ~A & B
    
    #Second type of carry out equation (B-A)
    #Borrow = A & ~B
 
    # printing the values
    print ("Difference = ", Difference)
    print ("Borrow = ", Borrow)
 
 
# Driver code
A = int(input ("Enter the value A:"))
B = int(input ("Enter the value B:"))

# passing three inputs of fulladder as arguments to get result function
Halfsubtractor (A, B)


#log value:-
  1) Enter the value A:0 
     Enter the value B:0
     Difference =  0
     Borrow =  0
  2) Enter the value A:0 
     Enter the value B:1
     Difference =  1
     Borrow =  1
  3) Enter the value A:1 
     Enter the value B:0
     Difference =  1
     Borrow =  0
  4) Enter the value A:1 
     Enter the value B:1
     Difference =  0
     Borrow =  0
