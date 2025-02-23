def checkArmstrong(n):
  originalNumber = n
  count = len(str(n))
  number = 0
  while n > 0:
    lastDigit = n % 10
    n = n // 10
    number = (number + lastDigit ** count)
  
  if number == originalNumber:
    return True
  else:
    return False
if __name__ == "__main__":
  t = int(input("Enter the number of test cases : "))
  for _ in range(t):
    n = int(input("Enter the number : "))
    print(checkArmstrong(n))