#te the factorial of a user-input number using a for loop, then rewrite it using a while loop, and compare their syntactic clarity.
# Factorial using a for loop
def factorial_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Factorial using a while loop
def factorial_while_loop(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result
# Get user input
num = int(input("Enter a non-negative integer: "))
# Calculate factorial using for loop
fact_for = factorial_for_loop(num)
print(f"Factorial of {num} using for loop is: {fact_for}")
# Calculate factorial using while loop
fact_while = factorial_while_loop(num)
print(f"Factorial of {num} using while loop is: {fact_while}")
