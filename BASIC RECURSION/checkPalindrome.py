import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        def check_palindrome(left: int, right: int) -> bool:
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return check_palindrome(left + 1, right - 1)
        
        return check_palindrome(0, len(s) - 1)

# Driver Code
import sys

def main():
    # Read the number of test cases
    tc = int(input().strip())

    while tc > 0:
        # Read the input string
        s = input().strip()

        # Create a Solution object
        obj = Solution()

        # Check if the string is a palindrome
        result = obj.isPalindrome(s)

        # Print the result
        print(result)
        
        tc -= 1
        print("~")

if __name__ == "__main__":
    main()
