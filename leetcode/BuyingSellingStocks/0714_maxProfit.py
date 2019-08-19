from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices)<=1:
            return 0
        l = len(prices)
        # baseline
        dp_1 = -prices[0] - fee
        dp_0 = 0
        for i in range(1, l):
            dp_1 = max([dp_1, dp_0 - prices[i] - fee])
            dp_0 = max([dp_0, dp_1 + prices[i]])
        return dp_0



if __name__ == '__main__':

    sol = Solution()

    prices = [1, 3, 2, 8, 4, 9]
    fee = 2

    print(sol.maxProfit(prices, fee))  # 8
