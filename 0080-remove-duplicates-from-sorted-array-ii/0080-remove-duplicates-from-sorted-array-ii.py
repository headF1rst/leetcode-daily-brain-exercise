from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = []
        dic = defaultdict(int)
        
        for num in nums:
            dic[num] += 1
        
        idx = 0
        for k, v in dic.items():
            if v == 1:
                nums[idx] = k
                idx += 1
            else:
                nums[idx] = k
                idx += 1
                nums[idx] = k
                idx += 1
        
        return idx