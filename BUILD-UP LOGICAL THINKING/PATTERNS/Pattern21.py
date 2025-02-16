def displayPattern(n):
    for i in range(n):  # Iterate over rows
        for j in range(n):  # Iterate over columns
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:  # Check if it's a border
                print("*", end="")  # Print star
            else:
                print(" ", end="")  # Print space
        print()  # Move to the next line

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))  # Number of test cases
    for _ in range(t):
        n = int(input("Enter the number of levels: "))  # Get input for size
        displayPattern(n)  # Print the pattern
