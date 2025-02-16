def displayPattern(n):
  num = 1
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(num, end = " ")
      num = num + 1
    print()    

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of levels: "))
        displayPattern(n)