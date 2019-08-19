class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        d = [[0] * (l2+1) for i in range(l1+1)]

        for i in range(l1+1):
            d[i][0] = i
        for j in range(l2+1):
            d[0][j] = j
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1])
                else:
                    d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+1+1)
        return d[l1][l2]


if __name__ == '__main__':

    s1 = 'sea'
    s2 = 'eat'

    sol = Solution()
    print(sol.minDistance(s1, s2))