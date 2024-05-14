# sum the series 1+1/2+1/3.........+1/n
n = int(input("Enter the value of n: "))
sum_series = 0

for i in range(1, n + 1):
    sum_series += 1 / i

print("Sum of the series:", sum_series)



#sum the series 1*1+1/2*2+1/3*3........+1/n*n
n = int(input("Enter the value of n: "))
sum_series = 0

for i in range(1, n + 1):
    sum_series += 1 / i * i

print("Sum of the series:", sum_series)

# # wap to calculate pow(x,n)

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

result = 1

for _ in range(abs(n)):
    result *= x

if n < 0:
    result = 1 / result

print("Result:", result)

#print the following pattern
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
