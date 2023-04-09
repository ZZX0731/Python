# 动态规划

"""
    求给定数组的最长递增子序列的长度，如[1,5,2,4,3]，最长递增子序列为1,2,4;或1,2,3，返回3
"""

# 优化
memo = {}


def Max_length(nums, i):
    """返回当前数组从下标i开始的最长递增子序列的长度"""
    if i in memo:
        return memo[i]
    if i == len(nums) - 1:
        return 1
    max_len = 1
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, Max_length(nums, j) + 1)
    memo[i] = max_len
    return max_len


def Length_of_LIS(nums):
    return max(Max_length(nums, i) for i in range(len(nums)))


# 最优解,复杂度n^2
def Length_of_LIS_ex(nums):
    n = len(nums)
    L = [1] * 5
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                L[i] = max(L[i], L[j] + 1)
    return max(L)


if __name__ == "__main__":
    array = [1, 5, 2, 4, 3]
    print(Length_of_LIS_ex(array))
