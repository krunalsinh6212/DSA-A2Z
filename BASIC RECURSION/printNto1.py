class Solution:
    #Complete this function
    def printNos(self, n):
        # Base case
        if n == 0:
            return
        # Recursive case: first call the function for n-1, then print n
        print(n, end=' ')
        self.printNos(n - 1)

#{ 
# Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        ob = Solution()

        ob.printNos(N)
        print()
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
