class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = 0

        for i in range(n):
            if i < n - 1 and dic[s[i]] < dic[s[i + 1]]:
                answer -= dic[s[i]]
            else:
                answer += dic[s[i]]
        
        return answer