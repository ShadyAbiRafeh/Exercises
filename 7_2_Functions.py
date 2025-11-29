#Implement the recursive Fibonacci sequence function, tracing the function calls for fib(4) to clearly illustrate the call stack and the base case.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        #base case is n=0 and n=1
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci sequence for n=4: {fibonacci(4)}")