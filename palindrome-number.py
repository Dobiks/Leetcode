class Solution:
    def isPalindrome(self, x: int) -> bool:
        if list(str(x))[::-1]==list(str(x)): return True
        else: return False
        
    
'''
Runtime: 74 ms, faster than 63.38% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 72.36% of Python3 online submissions for Palindrome Number.
'''