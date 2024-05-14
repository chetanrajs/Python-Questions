a=float(input("Enter the value for first side:"))
b=float(input("Enter the value for second side:"))
c=float(input("Enter the value for third side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is %0.2f"%area)