def reverseNumber(n):
  reversedNumber = 0
  while n > 0:
    lastDigit = n % 10
    n = n // 10
    reversedNumber = (reversedNumber * 10) + lastDigit
  return reversedNumber
if __name__ == "__main__":
  t = int(input("Enter the number of test cases : "))
  for _ in range(t):
    n = int(input("Enter the number : "))
    print(reverseNumber(n))
  