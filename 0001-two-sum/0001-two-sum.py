from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        visited = defaultdict(bool)

        for i, num in enumerate(nums):
            need = target - num
            if visited[need]:
                return [i, dic[need]]
            dic[num] = i
            visited[num] = True
