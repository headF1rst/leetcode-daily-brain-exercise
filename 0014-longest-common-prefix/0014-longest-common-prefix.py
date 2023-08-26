class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        min_length = 201

        for s in strs:
            min_length = min(min_length, len(s))

        for i in range(min_length):
            common = strs[0][i]
            for s in strs[1:]:
                if s[i] != common:
                    return answer
            
            answer += common
        
        return answer