class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""

        for c in s:
            c = c.lower()
            if c.isalpha() or c.isdigit():
                ss += c
        
        reverse_ss = ss[::-1]

        if ss != reverse_ss:
            return False
        
        return True