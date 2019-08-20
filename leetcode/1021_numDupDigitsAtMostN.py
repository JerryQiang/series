import functools

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        arr = [int(s) for s in str(N+1)]
        res, l = 0, len(arr)

        @functools.lru_cache()
        def A(m, n):
            if n == 0:
                return 1
            else:
                return A(m, n-1) * (m-n+1)

        for i in range(1, l):
            res += 9 * A(9, i-1)

        # print(res)

        s = set()
        for i, num in enumerate(arr):
            for j in range(0 if i else 1, num):
                if j not in s:
                    res += A(9-i, l-1-i)
                    # print(res)
            if num in s:
                break
            s.add(num)
            # print("set", s)
        return N - res




if __name__ == '__main__':

    sol = Solution()

    N = 20
    print(sol.numDupDigitsAtMostN(N))  # 1

    N = 100
    print(sol.numDupDigitsAtMostN(N))  # 10

    N = 1000
    print(sol.numDupDigitsAtMostN(N))  # 262

    N = 110
    print(sol.numDupDigitsAtMostN(N))  # 12
