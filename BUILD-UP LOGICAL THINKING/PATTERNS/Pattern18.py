def displayPattern(N):
    for i in range(N):
        char = 64 + N  # ASCII of the Nth letter (C for N=3, A for N=1)
        for j in range(i + 1):
            print(chr(char - j), end=" ")  # Print characters in reverse order
        print()  # Move to the next line

if __name__ == "__main__":
    N = int(input())  # Read integer input
   

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        N = int(input("Enter the number of levels: "))
        displayPattern(N)