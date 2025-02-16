n = int(input())  # Read input number

# Starting from 10 down to 1
counter = 10

# Using while loop to print the table in reverse order
while counter >= 1:
    print(n * counter, end=' ')
    counter -= 1
    