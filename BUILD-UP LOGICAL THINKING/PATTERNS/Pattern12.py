def displayPattern(n):
    for i in range(1, n + 1):
        space = 2 * (n - i)  # Calculate spaces between the two number sequences
        
        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end=" ")

        # Print spaces
        for k in range(space):
            print(" ", end="")

        # Print numbers in descending order
        for j in range(i, 0, -1):
            print(j, end=" ")

        print()  # Move to the next line

if __name__ == "__main__":
    n = int(input("Enter number of levels: "))
    displayPattern(n)
