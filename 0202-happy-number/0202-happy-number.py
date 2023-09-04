from collections import defaultdict

class Solution:
    def isHappy(self, n: int) -> bool:

        visited = defaultdict(bool)
        
        while n != 1:
            if visited[n]:
                return False
            visited[n] = True

            n = str(n)
            tmp = 0

            for i in n:
                tmp += int(i) ** 2
            n = tmp
        
        return True
