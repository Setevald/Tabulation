def fibonacci(n):
    fib = [0] * (n+1)
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]

n = 15
print(f"Fibonacci of {n} is {fibonacci(n)}")