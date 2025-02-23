class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


# Driver Code Starts
import math

def main():
    T = int(input())  # Read number of test cases

    while T > 0:
        n = int(input())  # Read input
        ob = Solution()
        print(ob.fib(n))  # Print Fibonacci result
        T -= 1

if __name__ == "__main__":
    main()
# Driver Code Ends
