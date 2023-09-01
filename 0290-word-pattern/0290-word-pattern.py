from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = defaultdict(str)
        s_list = s.split()
        n = len(pattern)
        visited = []

        if len(pattern) != len(s_list):
            return False

        for i in range(len(s_list)):
            if dic[pattern[i]] == '' and s_list[i] not in visited:
                dic[pattern[i]] = s_list[i]
                visited.append(s_list[i])
            elif dic[pattern[i]] == s_list[i]:
                continue
            else:
                return False
        
        return True