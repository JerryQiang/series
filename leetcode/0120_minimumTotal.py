from typing import List

class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     # 每行保留至当前层的最小路径和
    #     # 相邻结点只考虑正下和右下方
    #     l = len(triangle)
    #     line = [0 for i in range(l)]
    #     line[0] = triangle[0][0]
    #     for i in range(1, l):
    #         line[i] = line[i-1] + triangle[i][i]
    #         for j in range(i-1, 0, -1):
    #             line[j] = min([line[j-1], line[j]]) + triangle[i][j]
    #         line[0] = line[0] + triangle[i][0]
    #         # print(line)
    #     return min(line)

    # 考虑空间优化，可以直接在triangle上修改
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 每行保留至当前层的最小路径和
        # 相邻结点只考虑正下和右下方
        l = len(triangle)
        for i in range(1, l):
            triangle[i][i] = triangle[i-1][i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                triangle[i][j] = min([triangle[i-1][j-1], triangle[i-1][j]]) + triangle[i][j]
            triangle[i][0] = triangle[i-1][0] + triangle[i][0]
            # print(line)
        return min(triangle[l-1])

if __name__ == '__main__':

    sol = Solution()

    tri = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(sol.minimumTotal(tri))  # 11

    tri = [
        [-1],
        [3, 2],
        [-3, 1, -1]
    ]
    print(sol.minimumTotal(tri))  # -1

    tri = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(sol.minimumTotal(tri))  # 11

