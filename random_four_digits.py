import random

# Generate a random 4-digit number of 0s and 1s
binary_str = ""
for i in range(4):
    binary_str += str(random.randint(0,1))

# Convert the binary number to base 10
decimal_num = int(binary_str, 2)

# Print the binary number and its decimal equivalent
print("Binary number:", binary_str)
print("Decimal equivalent:", decimal_num)
