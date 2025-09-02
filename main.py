# Welcome message
print("Hi! Welcome to the celcius and fahrenheit converter!\n")

# Conversion options message
print("What would you like to convert?\n")
print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius\n")

# User input for conversion choice
choice = input("Enter 1 or 2: ")

# Converts celcius to fahrenheit or vice versa based on user choice
if choice == '1':
    c = float(input("Enter temperature in Celcius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C is equal to {f}°F")
elif choice == '2':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F is equal to {c}°C")

# Handles invalid input
else:
    print("Invalid choice. Please enter 1 or 2.")