from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = defaultdict(str)
        visited = []

        for a, b in zip(s, t):
            if dic[a] == '':
                if b in visited:
                    return False
                dic[a] = b
                visited.append(b)
                continue
            elif dic[a] == b:
                continue
            return False
        
        return True
