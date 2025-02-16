def displayPattern(n):
  for i in range(n, 0, -1):
    for j in range(i):
      print(chr(65 + j), end = " ")
    print()    

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)