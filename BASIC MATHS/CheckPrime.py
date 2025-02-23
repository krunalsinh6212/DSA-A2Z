def checkPrime(n):
  if n < 2:
    return False
  if n == 2:
      return True
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

if __name__ == "__main__":
  t = int(input("Enter the number of test cases : "))
  for _ in range(t):
    n = int(input("Enter the number : "))
    print(checkPrime(n))