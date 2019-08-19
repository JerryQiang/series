from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        l = len(prices)
        # baseline
        dp_1 = -prices[0]
        dp_0 = 0
        temp = 0
        for i in range(1, l):
            dp_1 = max([dp_1, temp - prices[i]])
            temp = dp_0
            dp_0 = max([dp_0, dp_1 + prices[i]])
        return dp_0



if __name__ == '__main__':

    sol = Solution()

    arr = [1, 2, 3, 0, 2]
    print(sol.maxProfit(arr))  # 3
