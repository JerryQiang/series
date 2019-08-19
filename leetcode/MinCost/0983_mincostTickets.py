from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if not days:
            return 0
        else:
            day_set = set(days)
            res = [0] * (days[-1] + 29)
            for i in range(len(res)):
                if i in day_set:
                    res[i] = min(res[i-1]+costs[0], res[i-7]+costs[1], res[i-30]+costs[2])
                else:
                    res[i] = res[i-1]
            return res[-1]

if __name__ == '__main__':

    sol = Solution()

    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]

    print(sol.mincostTickets(days, costs))  # 11

    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2,7,15]

    print(sol.mincostTickets(days, costs))  # 17