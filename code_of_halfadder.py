# example of half adder.

# Function to print sum and carry
def adder(a,b):
    
    # Calculating value of sum
    sum =a^b
    # Calculating value of carry
    carry=a&b
    
    # printing the values
    print ("sum", "carry", sum, carry)
    
# Driver code    
a= int(input ("number1 :"))
b= int(input ("number2 :"))

# passing two inputs of halfadder as arguments to get result function    
adder(a,b)

# complier output:
number1 :1
number2 :1
sum carry 0 1


# Function to print sum and carry
def getResult(A, B):
   
    # Calculating value of sum
    Sum = A ^ B
     
    # Calculating value of Carry
    Carry = A & B
     
    # printing the values
    print("Sum ", Sum)
    print("Carry", Carry)
 
 
# Driver code
A = int(input("Enter the value of a :"))
B = int(input("Enter the value of b :"))
 
# passing two inputs of halfadder as arguments to get result function
getResult(A, B)

#log value:- 
Enter the value of a :1
Enter the value of b :11
Sum  10
Carry 1
