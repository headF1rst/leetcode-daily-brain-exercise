from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = defaultdict(int)

        for s in magazine:
            dic[s] += 1
        
        for s in ransomNote:
            if dic[s] <= 0:
                return False
            dic[s] -= 1
        
        return True