def displayPattern(n):
    for i in range(1, 2 * n - 1):
      stars = i
      if (i > n):
        stars = 2 * n - i
      for j in range(1, stars):
        print("*", end="")
      print()

      


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)
