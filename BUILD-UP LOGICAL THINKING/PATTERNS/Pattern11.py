def displayPattern(n):
    for i in range(n):
      if (i % 2 == 0):
        start = 1
      else:
        start = 0
      for j in range(0, i + 1):
        print(start, end=" ")
        start = 1 - start
      print()

      


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)
