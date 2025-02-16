def displayPattern(n):
    for i in range(n):
        # spaces
        for j in range(i):
            print(" ", end="")

        # stars
        for j in range(2 * n - 2 * i - 1):
            print("*", end="")

        # move to next line
        print()


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)
