from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        max_profit = 0
        flag = False
        for i in range(1, l):
            if prices[i] > prices[i-1]:
                flag = True
                break
        if flag:
            for i in range(l-1):
                num = prices[i]
                for j in range(i, l):
                    profit = prices[j] - num
                    if profit > max_profit:
                        max_profit = profit

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        l = len(prices)
        min_value = prices[0]
        max_profit = 0
        for i in range(1, l):
            if prices[i] - min_value > max_profit:
                max_profit = prices[i] - min_value
            elif prices[i] < min_value:
                min_value = prices[i]
        return max_profit



if __name__ == '__main__':

    sol = Solution()

    arr = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(arr))  # 5

    arr = [7, 6, 4, 3, 1]
    print(sol.maxProfit(arr))  # 0