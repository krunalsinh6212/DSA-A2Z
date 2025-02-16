def displayPattern(n):
  for i in range(0, n):
    for j in range(1, n - i + 1):
      print("*", end=" ")
    print("\n")


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)
