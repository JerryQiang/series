from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 每行保留至当前层的最小路径和
        # 相邻结点考虑左下、正下和右下方
        l = len(triangle)
        if l == 1:
            return triangle[0][0]
        elif l == 2:
            return min([triangle[1][0], triangle[1][1]]) + triangle[0][0]
        else:
            line = [0 for i in range(l)]
            line[0] = triangle[0][0] + triangle[1][0]
            line[1] = triangle[0][0] + triangle[1][1]
            print(line)
            for i in range(2, l):
                res = [0 for i in range(l)]
                res[0] = min(line[0], line[1]) + triangle[i][0]
                for j in range(1, i-1):
                    res[j] = min([line[j-1], line[j], line[j+1]]) + triangle[i][j]
                res[i-1] = min(line[i - 2], line[i - 1]) + triangle[i][i-1]
                res[i] = line[i-1] + triangle[i][i]
                line = res
                print(line)
            return min(line)



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
