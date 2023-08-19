from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter(nums)

        idx = 0
        for k, v in counter.items():
            nums[idx] = k
            idx += 1
            if v >= 2:
                nums[idx] = k
                idx += 1

        return idx