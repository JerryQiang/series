from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_size = amount + 1
        dp = [max_size] * max_size
        dp[0] = 0
        for i in range(1, max_size):
            min = dp[i]
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    if dp[i-coins[j]] + 1 < min:
                        min = dp[i-coins[j]] + 1
            dp[i] = min
        # print("max_size", max_size)
        # print(dp)
        if dp[-1] >= max_size:
            return -1
        else:
            return dp[-1]


if __name__ == '__main__':

    sol = Solution()

    coins = [1, 2, 5]
    amount = 11
    print(sol.coinChange(coins, amount))  # 3

    coins = [2]
    amount = 3
    print(sol.coinChange(coins, amount))  # -1
