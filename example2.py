#Exercise 2: Find Prime Numbers in a List

# Step 1: Define a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Step 2: Ask the user for a list of numbers
numbers = input("Enter a list of numbers spereated by commas ").split(",")


# Step 3: Loop through the list and find prime numbers
primes = []
for num in numbers:
    num = int(num.strip())
    if is_prime(num):
        primes.append(num)
        

# Step 4: Print the list of prime numbers

print(f"The prime numbers are: {primes}")

