"""
    给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。
    找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
    返回容器可以储存的最大水量。
    说明：你不能倾斜容器。

"""


def Solution(arr: list[int]):
    i = 0
    j = len(arr) - 1
    Max = (j - i) * min(arr[i], arr[j])
    while i < j:
        if arr[i] < arr[i + 1]:
            i += 1
        else:
            j -= 1
        temp = (j - i) * min(arr[i], arr[j])
        Max = Max if Max > temp else temp
    return Max


if __name__ == "__main__":
    print(Solution([1, 8, 6, 2, 5, 4, 8, 3, 7]))
