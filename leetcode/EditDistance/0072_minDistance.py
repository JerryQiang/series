class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        d = [[0] * (n+1) for i in range(m+1)]
        # print(d)
        for i in range(m+1):
            d[i][0] = i
        for j in range(n+1):
            d[0][j] = j
        # print(d)
        for i in range(1, m+1):
            for j in range(1, n+1):
                left = d[i-1][j] + 1
                down = d[i][j-1] + 1
                left_down = d[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    left_down += 1
                d[i][j] = min([left, down, left_down])
                # print(left, down, left_down)
                # print(i, j, d[i][j])
        # print(d)
        return d[m][n]

    # 计算优化
    def minDistance_opt_count(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        d = [[0] * (n+1) for i in range(m+1)]

        for i in range(m+1):
            d[i][0] = i
        for j in range(n+1):
            d[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] != word2[j-1]:
                    d[i][j] = min([d[i-1][j], d[i][j-1], d[i-1][j-1]]) + 1
                else:
                    d[i][j] = min([d[i - 1][j], d[i][j - 1], d[i - 1][j - 1] - 1]) + 1
        return d[m][n]

    # o(n)内存优化
    def minDistance_opt_space(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        dm = 0
        dn = [0] * (n + 1)
        for j in range(n + 1):
            dn[j] = j

        for i in range(1, m + 1):
            dm = dn[0]
            dn[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] != word2[j - 1]:
                    res = min([dn[j], dn[j - 1], dm]) + 1
                else:
                    res = min([dn[j], dn[j - 1], dm - 1]) + 1
                dm = dn[j]
                dn[j] = res

        return dn[n]



if __name__ == '__main__':

    # word1 = "horse"
    # word2 = "ros"
    # sol = Solution()
    # print(sol.minDistance(word1, word2))
    #
    # word1 = "intention"
    # word2 = "execution"
    # sol = Solution()
    # print(sol.minDistance(word1, word2))

    # word1 = "horse"
    # word2 = "ros"
    # sol = Solution()
    # print(sol.minDistance_opt_count(word1, word2))
    #
    # word1 = "intention"
    # word2 = "execution"
    # sol = Solution()
    # print(sol.minDistance_opt_count(word1, word2))

    word1 = "horse"
    word2 = "ros"
    sol = Solution()
    print(sol.minDistance_opt_space(word1, word2))

    word1 = "intention"
    word2 = "execution"
    sol = Solution()
    print(sol.minDistance_opt_space(word1, word2))