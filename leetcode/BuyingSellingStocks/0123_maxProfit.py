from typing import List

class Solution:
    # 0 ~ l-1的最大利润 = max{0~i, i+1~l-1}
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        l = len(prices)
        start_profit = [0] * l
        end_profit = [0] * l
        # [0, i]单次交易最大利润
        # i: 0 - l-1
        min_value = prices[0]
        for i in range(1, l):
            if prices[i] < min_value:
                min_value = prices[i]
                start_profit[i] = start_profit[i - 1]
            else:
                start_profit[i] = max([start_profit[i-1], prices[i] - min_value])

        # [i, l-1]单次交易最大利润
        # i: 0 - l-1
        max_value = prices[-1]
        for i in range(l-2, -1, -1):
            if prices[i] > max_value:
                max_value = prices[i]
                end_profit[i] = end_profit[i+1]
            else:
                end_profit[i] = max([end_profit[i+1], max_value - prices[i]])

        # 求最大利润
        # print(start_profit)
        # print(end_profit)
        # print(start_profit[-1], end_profit[0])
        max_profit = start_profit[-1]
        for i in range(1, l-1):
            if start_profit[i] + end_profit[i+1] > max_profit:
                max_profit = start_profit[i] + end_profit[i+1]

        return max_profit


if __name__ == '__main__':

    sol = Solution()

    arr = [3, 3, 5, 0, 0, 3, 1, 4]
    print(sol.maxProfit(arr))  # 6

    arr = [1, 2, 3, 4, 5]
    print(sol.maxProfit(arr))  # 4

    arr = [7, 6, 4, 3, 1]
    print(sol.maxProfit(arr))  # 0