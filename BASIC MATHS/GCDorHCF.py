def gcd(n1, n2):
  gcd = 1
  for i in range(1, min(n1, n2) + 1):
    if (n1 % i == 0 and n2 % i == 0):
      gcd = i
  return gcd



if __name__ == "__main__":
  t = int(input("Enter the number of test cases : "))
  for _ in range(t):
    n1 = int(input("Enter the number : "))
    n2 = int(input("Enter the number : "))
  print(gcd(n1, n2))
