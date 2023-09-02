from collections import defaultdict

class Solution:
    def isAnagram(self, ss: str, tt: str) -> bool:
        if len(ss) != len(tt):
            return False
        
        dic = defaultdict(int)
        for s in ss:
            dic[s] += 1
        
        for t in tt:
            if dic[t] == 0:
                return False
            dic[t] -= 1
        
        return True
