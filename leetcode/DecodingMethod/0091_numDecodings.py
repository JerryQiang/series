class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if l == 1:
            num = int(s)
            if num != 0:
                return 1
            else:
                return 0
        elif l == 2:
            if s[0] == '0':
                return 0
            num = int(s)
            if s[1] == '0' and num != 10 and num != 20:
                return 0
            elif num == 10 or num == 20 or num >= 27:
                return 1
            else:
                return 2
        else:
            dp = [0] * l
            if s[0] == '0':
                return 0
            else:
                dp[0] = 1
            num = int(s[:2])
            if s[1] == '0':
                if num==10 or num==20:
                    dp[1] = 1
                else:
                    return 0
            else:
                if num >= 27:
                    dp[1] = 1
                else:
                    dp[1] = 2
            for i in range(2, l):
                if s[i] == '0':
                    dp[i-1] = 0
                num = int(s[i-1:i+1])
                if num == 0:
                    return 0
                elif num < 10 or num > 26:
                    dp[i-2] = 0
                dp[i] = dp[i-1]+dp[i-2]
            return dp[l-1]


    # https://leetcode-cn.com/problems/decode-ways/solution/4-xing-python-dp-onshi-jian-o1kong-jian-by-qqqun90/
    # 规则简写
    def numDecodings(self, s: str) -> int:
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (10 <= int(s[i-1: i+1]) <= 26) + p * (s[i]!='0')
        return p




if __name__ == '__main__':

    sol = Solution()

    msg = '12'
    print(sol.numDecodings(msg))  # 2

    msg = '226'
    print(sol.numDecodings(msg))  # 3

    msg = '110'
    print(sol.numDecodings(msg))  # 1

    msg = '227'
    print(sol.numDecodings(msg))  # 2

    msg = '301'
    print(sol.numDecodings(msg))  # 0

    msg = '30'
    print(sol.numDecodings(msg))  # 0

    msg = '20'
    print(sol.numDecodings(msg))  # 1

    msg = '0'
    print(sol.numDecodings(msg))  # 0