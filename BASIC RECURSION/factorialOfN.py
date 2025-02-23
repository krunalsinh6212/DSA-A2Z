class Solution:
    def factorialNumbers(self, n):
        result = []
        fact = 1
        i = 1
        
        while fact <= n:
            result.append(fact)
            i += 1
            fact *= i  # Compute next factorial
        
        return result

# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print("\n~")
