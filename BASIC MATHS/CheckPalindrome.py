def checkPalindrome(n):
  n = str(n)
  reversedNumber = n[::-1]
  if reversedNumber == n:
    return True
  else:
    return False
if __name__ == "__main__":
  t = int(input("Enter the number of test cases : "))
  for _ in range(t):
    n = int(input("Enter the number : "))
    print(checkPalindrome(n))