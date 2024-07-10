def generate_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end="")
        # Print numbers in descending order
        for k in range(i - 1, 0, -1):
            print(k, end="")
        # Move to the next line for the next row
        print()

# Function to test the pattern
def test_pyramid():
    print("Testing Pyramid Pattern:")
    generate_pyramid(5)  # You can adjust the number of rows here

# Test the pattern
test_pyramid()
