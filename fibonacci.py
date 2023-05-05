# Function to calculate the Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# Calculate the sum of the first 50 Fibonacci numbers
sum = 0
for i in range(1, 51):
    fib_num = fibonacci(i)
    sum += fib_num

# Print the sum
print("The sum of the first 50 Fibonacci numbers is:", sum)
