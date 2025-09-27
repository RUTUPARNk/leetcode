class Solution:
    def isPalindrome(self, s: str) -> bool:
        filr = ''.join(c.lower() for c in s if c.isalnum())
        return filr == filr[::-1]