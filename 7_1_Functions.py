#Compute Average with error handling
def compute_average(data_list):
    if not data_list:
        return 0 # Return 0 for empty list to avoid division by zero
    return sum(data_list) / len(data_list)
grades1 = [85, 90, 78, 92, 88]
grades2 = []

print(f"Average of grades: {compute_average(grades1)}")
print(f"Average of grades (empty list): {compute_average(grades2)}")