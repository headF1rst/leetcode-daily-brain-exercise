from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            if len(indices[num]) > 0 and abs(indices[num][-1] - i) <= k:
                return True
            else:
                indices[num].append(i)

        return False