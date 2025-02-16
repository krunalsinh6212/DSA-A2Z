def displayPattern(n):
    spaces = 2 * n - 2  # Initial spaces
    
    for i in range(1, 2 * n):  # Loop for full pattern
        stars = i if i <= n else (2 * n - i)  # Star count logic

        # Print first set of stars
        for j in range(stars):
            print("*", end="")

        # Print spaces
        for k in range(spaces):
            print(" ", end="")

        # Print second set of stars
        for j in range(stars):
            print("*", end="")

        print()  # Move to next line

        # Adjust spaces dynamically
        if i < n:
            spaces -= 2  # Decrease spaces in first half
        else:
            spaces += 2  # Increase spaces in second half

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)
