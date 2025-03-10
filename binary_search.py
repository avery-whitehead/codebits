def binary_search(nums: list[int], n: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == n:
            return middle
        elif nums[middle] < n:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def find_sqrt(x: int) -> int:
    left = 1
    right = x

    while left <= right:
        middle = (left + right) // 2
        if middle * middle == x:
            return middle
        elif middle * middle < x:
            left = middle + 1
        else:
            right = middle - 1

    return right


print(find_sqrt(2147395599))
