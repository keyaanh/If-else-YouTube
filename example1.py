#Exercise 1: Check if a Number is Even or Odd
# Step 1: Ask the user for a number
# - Use the input() function to get the number from the user.
# - Convert the input from a string to an integer using int().

# Step 2: Check if the number is even or odd
# - Use the modulo operator (%) to check if the number is divisible by 2.
# - If the remainder is 0, the number is even.
# - Otherwise, the number is odd.

# Step 3: Print the result
# - Use an if-else statement to display whether the number is even or odd.
# - Test with different numbers to verify your program works.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

