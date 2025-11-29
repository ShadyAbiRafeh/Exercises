#Use filter() with a lambda function to select and return only the odd numbers from a given list of integers.
numbers = [1, 2 ,3 ,4 ,5]

#Define a lambda function to square a number
square_lambda = lambda x:x ** 2

#use map() to apply the lambda function to each number in the list
squared_numbers = list(map(square_lambda, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared numbers (using map and lambda): {squared_numbers}")