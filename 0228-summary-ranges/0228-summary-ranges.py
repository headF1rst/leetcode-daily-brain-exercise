class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        n = len(nums)
        over_two = False
        start = -1

        if n == 1:
            return [str(nums[0])]

        for i in range(n - 1):
            if nums[i] != nums[i + 1] - 1:
                if not over_two:
                    answer.append(str(nums[i]))
                else:
                    answer.append(str(start) + "->" + str(nums[i]))
                start = -1
                over_two = False
            else:
                if start == -1:
                    start = nums[i]
                    over_two = True

        if n > 1:
            if not over_two:
                answer.append(str(nums[-1]))
            else:
                answer.append(str(start) + "->" + str(nums[-1]))

        return answer
                 
