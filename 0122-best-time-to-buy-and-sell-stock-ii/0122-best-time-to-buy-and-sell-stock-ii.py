class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        profit = prices[0]

        for price in prices[1:]:
            if profit > price:
                profit = price
            else:
                answer += price - profit
                profit = price
        
        return answer