n = int(input("Enter the value for n: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
average = sum / n
print(f"Average of the first {n} natural numbers: {average}")