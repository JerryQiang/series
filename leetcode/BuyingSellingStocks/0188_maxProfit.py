from typing import List
import sys

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        l = len(prices)
        if k > l:
            dp_i_0 = 0
            for i in range(l):
                # baseline
                if i == 0:
                    dp_i_1 = -prices[0]  # dp[0][1] = -prices[0]
                    dp_i_0 = 0  # dp[0][0] = 0
                dp_i_1 = max([dp_i_1, dp_i_0 - prices[i]])
                dp_i_0 = max([dp_i_0, dp_i_1 + prices[i]])
            return dp_i_0
        else:
            dp = [[[0, 0] for j in range(k+1)] for i in range(l)]  # l * (k+1) * 2
            for i in range(l):
                dp[i][0][1] = -sys.maxsize-1
                for j in range(1, k+1):
                    if i == 0:
                        dp[i][j][1] = -prices[i]
                        dp[i][j][0] = 0
                        continue
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
                    dp[i][j][0]= max([dp[i-1][j][0], dp[i-1][j][1] + prices[i]])
            return dp[l-1][k][0]


    def maxProfit(self, k: int, prices: List[int]) -> int:
        l = len(prices)
        if k > l:
            dp_i_0 = 0
            for i in range(l):
                # baseline
                if i == 0:
                    dp_i_1 = -prices[0]  # dp[0][1] = -prices[0]
                    dp_i_0 = 0  # dp[0][0] = 0
                dp_i_1 = max([dp_i_1, dp_i_0 - prices[i]])
                dp_i_0 = max([dp_i_0, dp_i_1 + prices[i]])
            return dp_i_0
        else:
            dp_i_0 = [[0, 0] for i in range(k+1)] # (k+1) * 2
            dp_i_0[0][1] = -sys.maxsize - 1
            for i in range(l):
                dp_i_1 = [[0, 0] for i in range(k + 1)]  # (k+1) * 2
                dp_i_1[0][1] = -sys.maxsize - 1
                for j in range(1, k+1):
                    if i==0:
                        dp_i_0[j][1] = -prices[i]
                        dp_i_0[j][0] = 0
                    dp_i_1[j][1] = max(dp_i_0[j][1], dp_i_0[j-1][0] - prices[i])
                    dp_i_1[j][0]= max([dp_i_0[j][0], dp_i_0[j][1] + prices[i]])
                dp_i_0 = dp_i_1
            return dp_i_0[k][0]






if __name__ == '__main__':

    sol = Solution()

    arr = [2, 4, 1]
    k = 2
    print(sol.maxProfit(2, arr))  # 2

    arr = [3,2,6,5,0,3]
    k = 2
    print(sol.maxProfit(2, arr))  # 7
