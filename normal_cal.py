#normal calculator.

#input a number.
a=int(input("User input a: "))
#input the required opertor
operation=input("operation(+,-,*,/,%): ")
#input the second user
b=int(input("User input b: "))

#opertion sequence 

if operation=="+":
    print (a+b);
elif operation=="-":
    print (a-b);
elif operation=="*":
    print (a*b);
elif operation=="/":
    print (a/b);
elif operation=="%":
    print (a%b);
else:
    print("Invalied Operation")
