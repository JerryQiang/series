from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1
        add_nums = []
        count = 0
        index = 0
        ln = len(nums)
        while n >= missing:
            if index < ln and nums[index] <= missing:
                missing += nums[index]
                index += 1
            else:
                add_nums.append(missing)
                count += 1
                missing += missing

            # print(missing)
        # print(add_nums)
        # print(count)
        return count


if __name__ == '__main__':

    solution = Solution()

    nums = [1,3]
    n = 6
    print(solution.minPatches(nums, n))

    nums = [1, 5, 10]
    n = 20
    print(solution.minPatches(nums, n))

    nums = [1, 2, 2]
    n = 5
    print(solution.minPatches(nums, n))