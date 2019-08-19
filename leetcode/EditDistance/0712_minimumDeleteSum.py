class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        d = [[0] * (l2+1) for i in range(l1+1)]
        d[0][0] = 0
        for i in range(1, l1+1):
            d[i][0] = d[i-1][0] + ord(s1[i-1])
        for j in range(1, l2+1):
            d[0][j] = d[0][j-1] + ord(s2[j-1])
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s1[i-1] == s2[j-1]:
                    d[i][j] = min(d[i-1][j]+ord(s1[i-1]), d[i][j-1]+ord(s2[j-1]), d[i-1][j-1])
                else:
                    d[i][j] = min(d[i-1][j]+ord(s1[i-1]), d[i][j-1]+ord(s2[j-1]), d[i-1][j-1]+ord(s1[i-1])+ord(s2[j-1]))
        return d[l1][l2]


if __name__ == '__main__':

    s1 = 'sea'
    s2 = 'eat'

    sol = Solution()
    print(sol.minimumDeleteSum(s1, s2))  # 231

    s1 = "xnbteodleejrzeo"
    s2 = "gaouojqkkk"
    print(sol.minimumDeleteSum(s1, s2))  # 2255