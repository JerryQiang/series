# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m_edge = len(matrix)
        n_edge = len(matrix[0])
        res = []
        for i in range((len(matrix)+1)//2):
            if m_edge==0 or n_edge==0:
                return res
            elif m_edge==1:
                for j in range(n_edge):
                    res.append(matrix[i][i + j])
                return res
            elif m_edge==1:
                for j in range(n_edge):
                    res.append(matrix[i][i + j])
                return res
            elif n_edge==1:
                for j in range(m_edge):
                    res.append(matrix[i+j][i+n_edge-1])
                return res
            else:
                for j in range(n_edge-1):
                    res.append(matrix[i][i+j])  # ->matrix[i][i+n_dge-1]

                for j in range(m_edge-1):
                    res.append(matrix[i+j][i+n_edge-1])  # ->matrix[i+m_dge-1][i+n_dge-1]

                for j in range(n_edge-1):
                    res.append(matrix[i+m_edge-1][i+n_edge-1-j])  # ->matrix[i+m_dge-1][i]

                for j in range(m_edge-1):
                    res.append(matrix[i+m_edge-1-j][i])  # ->matrix[i][i]
            m_edge -= 2
            n_edge -= 2
        return  res

    def printMatrix(self, matrix):
        # write code here
        res = []
        if matrix and matrix[0]:
            m = len(matrix)
            n = len(matrix[0])

            if m == 0 or n == 0:
                return res
            if m == 1 or n == 1:
                for i in matrix:
                    res += i
                return res
            else:
                for j in range(n):
                    res += [matrix[0].pop(0)]
                for i in range(1, m):
                    res += [matrix[i].pop(n - 1)]
                for j in range(2, n + 1):
                    res += [matrix[m - 1].pop(-1)]
                for i in range(2, m):
                    res += [matrix[-i].pop(0)]
                matrix.pop(0)
                matrix.pop(-1)
            return res + self.printMatrix(matrix)
        else:
            return res


if __name__ == '__main__':

    sol = Solution()

    arr = [[1, 2, 3 ,4],
           [5, 6, 7 ,8],
           [9, 10, 11 ,12],
           [13, 14, 15 ,16],]
    # print sol.printMatrix(arr)

    # arr = [[1]]
    # print sol.printMatrix((arr))
    #
    # arr = [[1], [2], [3], [4], [5]]
    # print sol.printMatrix((arr))
    #
    # arr = [[1,2],[3,4],[5,6],[7,8],[9,10]]
    # print sol.printMatrix(arr)
