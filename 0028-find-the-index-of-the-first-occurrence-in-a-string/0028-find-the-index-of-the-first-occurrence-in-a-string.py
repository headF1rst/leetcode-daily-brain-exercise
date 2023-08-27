class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        nn = len(haystack)

        for i in range(nn - n + 1):
            if haystack[i: i + n] == needle:
                return i

        return -1
