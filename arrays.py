def removeDuplicates(nums: list[int]) -> int:
    dupe_potential = float("-inf")
    k = 0
    for n in nums:
        if n == dupe_potential:
            k += 1
        else:
            nums[k] = n
        dupe_potential = n
    return k


removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
