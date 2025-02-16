def displayPattern(n):
    spaces = 0
    for i in range(n):
        # stars
        for j in range(1, n - i + 1):
            print("*", end=" ")
        
        # spaces
        for k in range(spaces):
            print(" ", end=" ")
        
        # stars
        for l in range(1, n - i + 1):
            print("*", end=" ")
        
        print()
        spaces += 2  # Increase spaces in each iteration

    spaces -= 2  # Adjust spaces before the second loop

    for i in range(1, n + 1):
        # stars
        for j in range(1, i + 1):
            print("*", end=" ")
        
        # spaces
        for k in range(spaces):
            print(" ", end=" ")
        
        # stars
        for l in range(1, i + 1):
            print("*", end=" ")
        
        print()
        spaces -= 2  # Decrease spaces in each iteration

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)
