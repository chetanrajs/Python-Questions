def fib(x):
    if x <= 1:
        return x
    else:
        return (fib(x - 1) + fib(x - 2))

n = int(input("Enter the number of terms in the Fibonacci series: "))
for i in range(n):
    print(fib(i), end="  ")