# Write a programme to swap a number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers with a temporary variable
temp = num1
num1 = num2
num2 = temp

print(f"After swapping: num1 = {num1}, num2 = {num2}")

