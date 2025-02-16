def displayPattern(n):
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end=" ")

        breakpoint = (2 * i + 1) // 2
        char = 65  # ASCII value for 'A'

        # Print characters in a pyramid pattern
        for j in range(2 * i + 1):
            print(chr(char), end=" ")
            if j < breakpoint:
                char += 1  # Increment character (A → B → C)
            else:
                char -= 1  # Decrement character (C → B → A)

        # Move to the next line
        print()


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)
