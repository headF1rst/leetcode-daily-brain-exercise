from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        q = deque(nums)
        n = len(nums)
        k %= n

        for _ in range(k):
            tmp = q.pop()
            q.appendleft(tmp)
        
        for i in range(n):
            nums[i] = q[i]