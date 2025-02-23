def sumN(n):
    if n == 0:
        return 0
    else:
        return n + sumN(n - 1)

n = int(input("Enter a number: "))
result = sumN(n)
print(f"The sum of the first {n} numbers is: {result}")
