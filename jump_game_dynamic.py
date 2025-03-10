def can_jump(nums: list[int]) -> bool:
    state: list[bool | None] = [None] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            state[i] = True
        elif nums[i] == 0:
            state[i] = False
        else:
            state[i] = any(state[i + 1 : i + 1 + nums[i]])

    return state[0] is True


print(can_jump([3, 1, 0, 1, 4]))
