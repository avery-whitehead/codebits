def partition(s: str) -> list[list[str]]:
    result: list[list[str]] = []
    partition: list[str] = []

    def dfs(i: int):
        if i >= len(s):
            result.append(partition[:])
            return
        for j in range(i, len(s)):
            if is_palindrome(s[i : j + 1]):
                partition.append(s[i : j + 1])
                dfs(j + 1)
                partition.pop()

    dfs(0)

    return result


def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


print(partition("aabaac"))
