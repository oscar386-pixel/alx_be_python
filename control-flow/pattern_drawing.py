# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use for loop to print '*' size times in one row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1  # Increment row counter
