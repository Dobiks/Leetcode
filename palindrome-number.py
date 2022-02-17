class Solution:
    def isPalindrome(self, x: int) -> bool:
        if list(str(x))[::-1]==list(str(x)): return True
        else: return False


s = Solution()
print(s.isPalindrome(x = 129))

