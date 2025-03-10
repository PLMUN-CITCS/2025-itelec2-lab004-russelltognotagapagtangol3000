# Russell Togno
# ITELEC2
# Laboratory #04 – Guided Coding Exercise:
# Input, Output, and Text Formatting in Python

# Get integer input from the user and convert it to an integer
user_integer = int(input("Enter an integer: "))

# Get float (decimal) input from the user and convert it to a float
user_decimal = float(input("Enter a decimal number: "))

# Get string input from the user (no conversion needed)
user_text = input("Enter a string: ")

# Display formatted output using old-style string formatting (% operator)
print("\nFormatted Output using old-style formatting:")
print("Integer: %d" % user_integer)
print("Decimal: %.2f" % user_decimal)  # Format decimal to 2 decimal places
print("String: %s" % user_text)

# Display formatted output using modern f-strings
print("\nFormatted Output using f-strings:")
print(f"Integer: {user_integer}")
print(f"Decimal: {user_decimal:.2f}")  # Format decimal to 2 decimal places
print(f"String: {user_text}")
