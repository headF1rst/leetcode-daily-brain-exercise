class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        strs.sort()
        first, last = strs[0], strs[-1]
        n = len(min(first, last))

        for i in range(n):
            if first[i] != last[i]:
                return answer
            
            answer += first[i]
        
        return answer