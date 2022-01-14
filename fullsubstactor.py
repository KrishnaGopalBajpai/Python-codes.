def fullsubstactor (A, B, C):
 
    # Calculating value of sum
    Sum = A ^ B ^ C
    
    # Calculating value of C-Out (A-B-C)
    C_Out = (~A & B)|(B & C)|(~A & C)
    
    #Second type of carry out equation (B-A-C)
    C_Out = (A & ~B)|(~B & C)|(A & C)
 
    # printing the values
    print("Sum = ", Sum)
    print("C-Out = ", C_Out)
 
 
# Driver code
A = int(input ("Enter the value A:"))
B = int(input ("Enter the value B:"))
C = int(input ("Enter the value C:"))
# passing three inputs of fulladder as arguments to get result function
fullsubstactor(A, B, C)
