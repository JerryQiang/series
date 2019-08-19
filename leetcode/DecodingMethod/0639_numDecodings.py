class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        pp = 1
        if s[0] == '0':
            p = 0
        elif s[0] == '*':
            p = 9
        else:# 1 - 9
            p = 1
        for i in range(1, l):
            # set a
            if s[i] == '0':
                a = 0
            elif s[i] == '*':
                a = 9
            else:  # 1 - 9
                a = 1

            # set b
            if s[i-1] == '0':  # 00 - 09:
                b = 0
            elif s[i-1] == '*':
                if s[i] == '*':  # 11 - 19, 21 - 26
                    b = 15
                elif int(s[i]) <= 6:  # 10, 20 or 11, 21 ... or 16, 26
                    b = 2
                # int(s[i])>=7
                else:
                    b = 1  # 17 - 19
            elif s[i] == '*':
                if s[i-1] == '1':  # 1*
                    b = 9
                elif s[i-1] == '2':  # 2*
                    b = 6
                else:
                    b = 0
            else:
                if 10 <= int(s[i-1:i+1]) <= 26:
                    b = 1
                else:  # 27 - 99
                    b = 0
            pp, p = p, a * p + b * pp  # dp[i] = a * dp[i-1] + b * dp[i-2]
            p = p % (10 ** 9 + 7)
        return p


if __name__ == '__main__':

    sol = Solution()

    msg = '*'
    print(sol.numDecodings(msg))  # 9

    msg = '1*'
    print(sol.numDecodings(msg))  # 18

    msg = '2*'
    print(sol.numDecodings(msg))  # 15


