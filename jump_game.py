def can_jump(nums: list[int]) -> bool:
    d: dict[int, bool] = {}

    if len(nums) == 1:
        return True

    def jump(idx: int, depth: int = 0) -> bool:
        print("|" * depth + f"> {idx}")
        if idx in d:
            print("|" * depth + f"& {d[idx]}")
            return d[idx]

        if idx == len(nums) - 1:
            d[idx] = True
            print("|" * depth + f"< {d[idx]}")
            return True

        if idx >= len(nums) or nums[idx] == 0:
            d[idx] = False
            print("|" * depth + f"< {d[idx]}")
            return False

        result = any(jump(idx + i, depth + 1) for i in range(1, nums[idx] + 1))
        d[idx] = result
        return result

    return jump(0)


def jump(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0

    def jump_inner(idx: int, depth: int = 0) -> int:
        if idx >= len(nums) - 1:
            return depth

        return min(
            jump_inner(idx + i, depth + 1) for i in range(1, nums[idx] + 1)
        )

    return jump_inner(0)


def jump_dp(nums: list[int]) -> int:
    max_int = 2**64
    # How many jumps do we need to get to the end?
    state: list[int] = [max_int for _ in nums]
    # 0 jumps to get to the end if we're already there
    state[-1] = 0
    for i in range(len(nums) - 2, -1, -1):
        # if we can reach the end from where we are, the end is 1 jump away
        if nums[i] + i >= len(nums) - 1:
            state[i] = 1
            continue
        # the end is one jump + the smallest of the states we can reach
        vals = [n for n in state[i + 1 : i + 1 + nums[i]]]
        if not vals:
            state[i] = max_int
            continue
        state[i] = 1 + min(vals)
    return state[0]


def jump_2(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0

    near = 0
    far = 0
    jumps = 0

    while far < len(nums) - 1:
        farthest = 0
        for i in range(near, far + 1):
            farthest = max(farthest, i + nums[i])
        near = far + 1
        far = farthest
        jumps += 1

    return jumps


# print(jump_2([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
# # fmt: off
# print(jump_2([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,3,8,5]))
# # fmt: on


# print(jump_dp([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
# # fmt: off
# print(jump_dp([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,3,8,5]))
# # fmt: on

print(jump_dp([2, 3, 0, 1, 4]))
