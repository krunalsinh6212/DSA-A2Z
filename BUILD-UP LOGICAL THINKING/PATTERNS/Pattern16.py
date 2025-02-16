def displayPattern(n):
  for i in range(n):
    for j in range(i + 1):
      print(chr(65 + i), end = " ")
    print()    

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)