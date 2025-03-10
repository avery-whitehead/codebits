def is_prime(n) -> bool:
    True


def is_perfect_power_2(n):
    exponent = 1
    while True:
        if 2**exponent > n:
            return False
        base = 1
        exponent = base
        while hi**exponent <= n:
            hi += 1
        while hi - lo > 1:
            middle = (lo + hi) // 2
            if middle**exponent <= n:
                lo = middle
            else:
                hi = middle
        if lo**exponent == n:
            return True
        exponent += 1
