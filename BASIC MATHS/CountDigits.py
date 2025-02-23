def countDigit(n):
  count = 0
  while n > 0:
    count += 1
    n = n // 10
  return count
if __name__ == "__main__":
  t = int(input("Enter the number of test cases : "))
  for _ in range(t):
    n = int(input("Enter the number : "))
    print(countDigit(n))
  