class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        end = 0
        n = len(s)

        for c in t:
            if end == n:
                return True
            if c == s[end]:
                end += 1

        if end == n:
            return True

        return False