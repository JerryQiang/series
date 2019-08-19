from typing import List

class Solution:
    # 多次交易
    # 多次波峰与波底差距之和
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        l = len(prices)
        profit = 0
        i = 1
        while i < l:
            while prices[i] <= prices[i - 1]:
                i += 1
                if i == l:
                    return profit
            min_value = prices[i - 1]
            while prices[i] > prices[i - 1]:
                i += 1
                if i == l:
                    profit += prices[i - 1] - min_value
                    return profit
            profit += prices[i - 1] - min_value
        return profit

    # 逻辑等价优化
    # 波峰和波谷的差值等于每一小段上升线段的累加值
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        l = len(prices)
        profit = 0
        for i in range(1, l):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp_i_0 = 0
        for i in range(l):
            # baseline
            if i == 0:
                dp_i_1 = -prices[0]  # dp[0][1] = -prices[0]
                dp_i_0 = 0  # dp[0][0] = 0
            dp_i_1 = max([dp_i_1, dp_i_0 - prices[i]])
            dp_i_0 = max([dp_i_0, dp_i_1 + prices[i]])
        return dp_i_0



if __name__ == '__main__':

    sol = Solution()

    arr = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(arr))  # 7

    arr = [7, 6, 4, 3, 1]
    print(sol.maxProfit(arr))  # 0