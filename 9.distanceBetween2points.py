import math
x1=float(input("Enter the value of x for first point:"))
y1=float(input("Enter the value of y for first point:"))
x2=float(input("Enter the value of x for second point:"))
y2=float(input("Enter the value of x for second point:"))

distance=math.sqrt(((x1-y1)**2)+((x2-y2)**2))
print("Distance between first and second point is %0.2f"%distance)