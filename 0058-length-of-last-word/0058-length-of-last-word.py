class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split()
        return len(tmp[-1])