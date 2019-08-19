from typing import List

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        l1 = len(A)
        l2 = len(B)
        dp = [[0] * (l2+1) for i in range(l1+1)]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l1][l2]


if __name__ == '__main__':

    sol = Solution()

    A = [1, 4, 2]
    B = [1, 2, 4]
    print(sol.maxUncrossedLines(A, B))  # 2

    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    print(sol.maxUncrossedLines(A, B))  # 3

    A = [1, 3, 7, 1, 7, 5]
    B = [1, 9, 2, 5, 1]
    print(sol.maxUncrossedLines(A, B))  # 2