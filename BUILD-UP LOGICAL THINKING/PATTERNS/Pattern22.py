def displayPattern(n):
    for i in range(0, 2 * n - 1):  # Iterate over rows
        for j in range(0, 2 * n - 1):  # Iterate over columns
            top = i
            left = j
            right = (2 * n - 2) - j
            down = (2 * n - 2) - i
            print(n - min(min(top, down), min(left, right)), end="")
        print()
if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))  # Number of test cases
    for _ in range(t):
        n = int(input("Enter the number of levels: "))  # Get input for size
        displayPattern(n)  # Print the pattern
