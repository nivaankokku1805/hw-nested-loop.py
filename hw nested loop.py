# Input: Decimal number
decimal_number = int(input("Enter a decimal number: "))

# Outer loop to handle the conversion
binary_number = ""
while decimal_number > 0:
    # Inner loop to calculate the remainder
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number //= 2

# Output: Binary number
print("Binary representation:", binary_number)